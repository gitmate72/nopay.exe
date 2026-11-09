#!/usr/bin/env bash
# One-time setup in a fresh cloud session (Playwright + Chromium are pre-installed there).
set -e
python3 -c "import cv2, scipy, faster_whisper" 2>/dev/null && { echo "deps ok"; exit 0; }
pip install --break-system-packages -q opencv-python-headless scipy numpy pillow faster-whisper
python3 -c "import cv2, scipy, faster_whisper; print('deps ok')"
