#!/usr/bin/env python3
"""Post the oldest queued reel. Runs in GitHub Actions (GH_TOKEN with contents:write + IG secrets).

Queue = folders on the "queue" branch: <YYYYMMDD-HHMM>-<slug>/reel.mp4 + caption.txt.
After a successful post: log it in posted/log.md on main, remove the folder, and rewrite the queue
branch as a single commit so posted videos don't pile up in git history.
To stop a reel, delete its folder on the queue branch before the posting time.
"""
import datetime, json, os, shutil, subprocess, sys, tempfile

REPO = os.environ['GITHUB_REPOSITORY']
TOKEN = os.environ['GH_TOKEN']
DRY = os.environ.get('DRY_RUN', 'false').lower() == 'true'
URL = f'https://x-access-token:{TOKEN}@github.com/{REPO}.git'


def git(*a, cwd=None):
    subprocess.run(['git', *a], cwd=cwd, check=True)


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
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%Y-%m-%d %H:%M IST')
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
