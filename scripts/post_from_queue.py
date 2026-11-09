#!/usr/bin/env python3
"""Post the oldest queued reel. Runs in GitHub Actions (needs GH_TOKEN for the repo + IG secrets).

Queue = GitHub Releases whose tag starts with "queue-" (e.g. queue-20261110-1300-zcad).
Each release has the video asset reel.mp4 and the caption as its release notes.
After a successful post: append to posted/log.md, commit, delete the release and its tag.
To stop a reel from going out, delete its release before the posting time.
"""
import json, os, subprocess, sys, tempfile, datetime

REPO = os.environ['GITHUB_REPOSITORY']
DRY = os.environ.get('DRY_RUN', 'false').lower() == 'true'


def gh(*args, capture=True):
    r = subprocess.run(['gh', *args], capture_output=capture, text=True)
    if r.returncode != 0:
        raise SystemExit(f'gh {" ".join(args)} failed: {r.stderr}')
    return r.stdout


rels = json.loads(gh('api', f'repos/{REPO}/releases?per_page=100'))
queue = sorted([r for r in rels if r['tag_name'].startswith('queue-') and not r['draft']], key=lambda r: r['tag_name'])
if not queue:
    print('::notice::Queue is empty, nothing to post.')
    sys.exit(0)
rel = queue[0]
tag = rel['tag_name']
asset = next((a for a in rel['assets'] if a['name'].endswith('.mp4')), None)
if not asset:
    raise SystemExit(f'{tag} has no .mp4 asset')
print(f'Posting {tag} ({len(queue)} in queue)')

with tempfile.TemporaryDirectory() as d:
    gh('release', 'download', tag, '--repo', REPO, '--pattern', asset['name'], '--dir', d)
    cap = os.path.join(d, 'caption.txt')
    open(cap, 'w', encoding='utf-8').write(rel['body'] or '')
    video = os.path.join(d, asset['name'])
    if DRY:
        print('DRY RUN: would post', video, 'with caption:\n', rel['body'])
        sys.exit(0)
    out = subprocess.run([sys.executable, 'scripts/post_reel.py', video, cap], capture_output=True, text=True)
    sys.stderr.write(out.stderr)
    if out.returncode != 0:
        raise SystemExit(out.stdout + out.stderr)
    res = json.loads(out.stdout.strip().splitlines()[-1])

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%Y-%m-%d %H:%M IST')
first = (rel['body'] or '').strip().splitlines()[0] if rel['body'] else ''
os.makedirs('posted', exist_ok=True)
with open('posted/log.md', 'a', encoding='utf-8') as f:
    f.write(f'| {now} | {tag} | {first} | {res.get("permalink", "")} |\n')
subprocess.run(['git', 'config', 'user.name', 'nopay-bot'], check=True)
subprocess.run(['git', 'config', 'user.email', 'nopay-bot@users.noreply.github.com'], check=True)
subprocess.run(['git', 'add', 'posted/log.md'], check=True)
subprocess.run(['git', 'commit', '-m', f'posted {tag}'], check=True)
subprocess.run(['git', 'push'], check=True)
gh('release', 'delete', tag, '--repo', REPO, '--yes', '--cleanup-tag')
print('Posted:', res)
