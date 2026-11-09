#!/usr/bin/env python3
"""Publish one MP4 as an Instagram Reel (Instagram API with Instagram Login, resumable upload).

usage: post_reel.py <video.mp4> <caption.txt> [cover_image_url]
env:   IG_ACCESS_TOKEN, IG_USER_ID, optional IG_API_VERSION (default v23.0)
prints JSON {"media_id": ..., "permalink": ...}
"""
import json, os, sys, time, urllib.parse, urllib.request, urllib.error

VER = os.environ.get('IG_API_VERSION', 'v23.0')
TOKEN = os.environ.get('IG_ACCESS_TOKEN', '').strip()
IGID = os.environ.get('IG_USER_ID', '').strip()
BASE = f'https://graph.instagram.com/{VER}'


def call(method, url, params=None, data=None, headers=None):
    if params:
        url += ('&' if '?' in url else '?') + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            return json.loads(r.read().decode() or '{}')
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors='replace')
        body = body.replace(TOKEN, '***') if TOKEN else body
        raise SystemExit(f'Instagram API error {e.code} on {method} {url.split("?")[0]}: {body}')


def main():
    if len(sys.argv) not in (3, 4):
        raise SystemExit(__doc__)
    if not TOKEN or not IGID:
        raise SystemExit('Missing IG_ACCESS_TOKEN or IG_USER_ID (add them as repository secrets).')
    video, cap_file = sys.argv[1], sys.argv[2]
    caption = open(cap_file, encoding='utf-8').read().strip()
    size = os.path.getsize(video)

    # 1) create a resumable REELS container
    params = {'media_type': 'REELS', 'upload_type': 'resumable', 'caption': caption,
              'share_to_feed': 'true', 'access_token': TOKEN}
    if len(sys.argv) == 4 and sys.argv[3]:
        params['cover_url'] = sys.argv[3]   # public image URL used as the reel cover / thumbnail
    c = call('POST', f'{BASE}/{IGID}/media', params=params)
    cid, uri = c['id'], c.get('uri') or f'https://rupload.facebook.com/ig-api-upload/{VER}/{c["id"]}'
    print('container', cid, file=sys.stderr)

    # 2) upload the bytes
    with open(video, 'rb') as f:
        data = f.read()
    up = call('POST', uri, data=data, headers={
        'Authorization': f'OAuth {TOKEN}', 'offset': '0', 'file_size': str(size),
        'Content-Type': 'application/octet-stream'})
    print('upload', up, file=sys.stderr)

    # 3) wait for processing
    for i in range(60):
        st = call('GET', f'{BASE}/{cid}', params={'fields': 'status_code,status', 'access_token': TOKEN})
        code = st.get('status_code')
        print('status', code, st.get('status', ''), file=sys.stderr)
        if code == 'FINISHED':
            break
        if code in ('ERROR', 'EXPIRED'):
            raise SystemExit(f'Instagram could not process the video: {st}')
        time.sleep(10)
    else:
        raise SystemExit('Timed out waiting for Instagram to process the video.')

    # 4) publish
    pub = call('POST', f'{BASE}/{IGID}/media_publish', params={'creation_id': cid, 'access_token': TOKEN})
    mid = pub['id']
    link = call('GET', f'{BASE}/{mid}', params={'fields': 'permalink', 'access_token': TOKEN}).get('permalink', '')
    print(json.dumps({'media_id': mid, 'permalink': link}))


if __name__ == '__main__':
    main()
