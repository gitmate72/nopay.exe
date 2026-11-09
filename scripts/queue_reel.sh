#!/usr/bin/env bash
# Put a finished reel in the posting queue = folder on the "queue" branch.
# usage: scripts/queue_reel.sh <reel_dir> <YYYYMMDD-HHMM> <slug>
# needs <reel_dir>/assets/reel.mp4 (< 95 MB) and <reel_dir>/caption.txt
set -euo pipefail
R="$(cd "$1" && pwd)"; SLOT="$2"; SLUG="$3"
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
URL="$(git -C "$ROOT" remote get-url origin)"
SIZE=$(stat -c %s "$R/assets/reel.mp4"); [ "$SIZE" -lt 95000000 ] || { echo "reel.mp4 too big ($SIZE bytes); re-encode with higher crf"; exit 1; }
Q="$(mktemp -d)/queue"
if git ls-remote --exit-code --heads "$URL" queue >/dev/null 2>&1; then
  git clone -q --depth 1 --branch queue "$URL" "$Q"
else
  mkdir -p "$Q" && git -C "$Q" init -q -b queue && git -C "$Q" remote add origin "$URL"
  printf '# Posting queue\nOne folder per reel: <YYYYMMDD-HHMM>-<slug>/reel.mp4 + caption.txt.\nThe oldest folder is posted next. Delete a folder to stop that reel.\n' > "$Q/README.md"
fi
D="$Q/$SLOT-$SLUG"; mkdir -p "$D"
cp "$R/assets/reel.mp4" "$D/reel.mp4"; cp "$R/caption.txt" "$D/caption.txt"
[ -f "$R/assets/cover.jpg" ] && cp "$R/assets/cover.jpg" "$D/cover.jpg"
git -C "$Q" add -A
git -C "$Q" -c user.name="nopay-bot" -c user.email="nopay-bot@users.noreply.github.com" commit -q -m "queue $SLOT-$SLUG"
git -C "$Q" push -q origin queue
echo "queued $SLOT-$SLUG"
ls "$Q" | grep -v README.md
