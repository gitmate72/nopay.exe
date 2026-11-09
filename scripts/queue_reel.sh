#!/usr/bin/env bash
# Put a finished reel in the posting queue (a GitHub Release).
# usage: scripts/queue_reel.sh <reel_dir> <YYYYMMDD-HHMM> <slug>
# needs <reel_dir>/assets/reel.mp4 and <reel_dir>/caption.txt
set -euo pipefail
R="$1"; SLOT="$2"; SLUG="$3"
TAG="queue-$SLOT-$SLUG"
gh release create "$TAG" "$R/assets/reel.mp4" --repo gitmate72/nopay.exe --title "$SLOT $SLUG" --notes-file "$R/caption.txt" --target main
echo "queued $TAG"
