#!/usr/bin/env python3
"""Post the oldest queued reel. Runs in GitHub Actions (GH_TOKEN with contents:write + IG secrets).

Queue = folders on the "queue" branch: <YYYYMMDD-HHMM>-<slug>/reel.mp4 + caption.txt.
After a successful post: log it in posted/log.md on main, remove the folder, and rewrite the queue
branch as a single commit so posted videos don't pile up in git history.
To stop a reel, delete its folder on the queue branch before the posting time.
"""
import datetime, json, os, random, re, shutil, subprocess, sys, tempfile
from zoneinfo import ZoneInfo

REPO = os.environ['GITHUB_REPOSITORY']
TOKEN = os.environ['GH_TOKEN']
DRY = os.environ.get('DRY_RUN', 'false').lower() == 'true'
URL = f'https://x-access-token:{TOKEN}@github.com/{REPO}.git'


def git(*a, cwd=None):
    subprocess.run(['git', *a], cwd=cwd, check=True)


# ---- one reel per day at a random US prime-time minute (scheduled runs only; manual runs post now) ----
ET = ZoneInfo('America/New_York')
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
if os.environ.get('SCHEDULED', 'false').lower() == 'true':
    now_et = datetime.datetime.now(ET)
    rnd = random.Random('nopay-' + now_et.strftime('%Y-%m-%d'))   # same random slot for every run of the day
    lo, hi = rnd.choice([(12 * 60, 14 * 60), (18 * 60, 21 * 60)])   # US lunch 12-2 pm or evening 6-9 pm ET
    target = rnd.randrange(lo, hi)
    mins = now_et.hour * 60 + now_et.minute
    print(f'ET now {now_et:%Y-%m-%d %H:%M}, today\'s slot {target // 60:02d}:{target % 60:02d} ET')
    if mins < target:
        print('::notice::Not time yet.'); sys.exit(0)
    for line in open('posted/log.md', encoding='utf-8'):
        m = re.match(r'\|\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) IST', line)
        if m and datetime.datetime.strptime(m.group(1), '%Y-%m-%d %H:%M').replace(tzinfo=IST).astimezone(ET).date() == now_et.date():
            print('::notice::Already posted today (US Eastern date).'); sys.exit(0)

q = tempfile.mkdtemp() + '/queue'
r = subprocess.run(['git', 'clone', '-q', '--depth', '1', '--branch', 'queue', URL, q], capture_output=True, text=True)
if r.returncode != 0:
    print('::notice::No queue branch yet, nothing to post.')
    sys.exit(0)
items = sorted(d for d in os.listdir(q) if os.path.isdir(os.path.join(q, d)) and not d.startswith('.')
               and os.path.exists(os.path.join(q, d, 'reel.mp4')))
if not items:
    print('::notice::Queue is empty, nothing to post.')
    sys.exit(0)
item = items[0]
video, cap = os.path.join(q, item, 'reel.mp4'), os.path.join(q, item, 'caption.txt')
caption = open(cap, encoding='utf-8').read().strip() if os.path.exists(cap) else ''
print(f'Posting {item} ({len(items)} in queue)')
if DRY:
    print('DRY RUN. Caption:\n' + caption)
    sys.exit(0)

args = [sys.executable, 'scripts/post_reel.py', video, cap]
if os.path.exists(os.path.join(q, item, 'cover.jpg')):   # repo is public, so Instagram can fetch the raw file
    args.append(f'https://raw.githubusercontent.com/{REPO}/queue/{item}/cover.jpg')
    print('cover:', args[-1])
env = dict(os.environ, VIDEO_URL=f'https://raw.githubusercontent.com/{REPO}/queue/{item}/reel.mp4')
out = subprocess.run(args, capture_output=True, text=True, env=env)
sys.stderr.write(out.stderr)
if out.returncode != 0:
    raise SystemExit(out.stdout + out.stderr)
res = json.loads(out.stdout.strip().splitlines()[-1])
print('Posted:', res)

# log on main
now = datetime.datetime.now(IST).strftime('%Y-%m-%d %H:%M IST')
first = caption.splitlines()[0].replace('|', '/') if caption else ''
with open('posted/log.md', 'a', encoding='utf-8') as f:
    f.write(f'| {now} | {item} | {first} | {res.get("permalink", "")} |\n')
for k, v in (('user.name', 'nopay-bot'), ('user.email', 'nopay-bot@users.noreply.github.com')):
    git('config', k, v); git('config', k, v, cwd=q)
git('add', 'posted/log.md'); git('commit', '-q', '-m', f'posted {item}'); git('push', '-q')

# drop the posted folder and squash the queue branch to one commit
shutil.rmtree(os.path.join(q, item))
git('checkout', '-q', '--orphan', 'fresh', cwd=q)
git('add', '-A', cwd=q)
git('commit', '-q', '--allow-empty', '-m', f'queue after posting {item}', cwd=q)
git('push', '-q', '-f', 'origin', 'fresh:queue', cwd=q)
