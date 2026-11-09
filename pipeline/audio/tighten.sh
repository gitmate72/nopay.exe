#!/usr/bin/env bash
# Trim long pauses and speed up the ElevenLabs voice, then get word timestamps.
# usage: pipeline/audio/tighten.sh <in.mp3> <reel_assets_dir>
set -euo pipefail
IN="$1"; A="$2"; mkdir -p "$A"
ffmpeg -v error -y -i "$IN" -af "silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-40dB:stop_silence=0.16,atempo=1.1" -ar 44100 "$A/vo.wav"
echo "voice seconds: $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$A/vo.wav")"
python3 "$(dirname "$0")/transcribe.py" "$A/vo.wav" "$A/words.json"
