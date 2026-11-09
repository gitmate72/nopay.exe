#!/usr/bin/env bash
# Render + mix + mux one reel.  usage: pipeline/build.sh reels/NNN-slug <duration_seconds> [workers]
# expects in the reel dir: reel.py, sfx.py, assets/vo.wav (tightened voice)
set -euo pipefail
R="$1"; DUR="$2"; WORK="${3:-6}"
A="$R/assets"; N=$(python3 -c "print(round($DUR*30))")
rm -rf "$A/frames"; mkdir -p "$A/frames"
per=$(( (N + WORK - 1) / WORK ))
for k in $(seq 0 $((WORK-1))); do
  a=$((k*per)); b=$(((k+1)*per)); [ $b -gt $N ] && b=$N; [ $a -ge $N ] && continue
  python3 "$R/reel.py" $a $b &
done; wait
got=$(ls "$A/frames" | wc -l); [ "$got" -eq "$N" ] || { echo "frames $got != $N"; exit 1; }
python3 "$R/sfx.py" "$A/fx.wav"
ffmpeg -v error -y -framerate 30 -i "$A/frames/%04d.jpg" -c:v libx264 -preset veryfast -crf 23 -pix_fmt yuv420p "$A/video.mp4"
# mix: normalise voice and fx separately, sidechain-duck fx, then final loudness (never chain all in one graph: it truncates)
ffmpeg -v error -y -i "$A/vo.wav" -af "apad=whole_dur=$DUR,loudnorm=I=-16:TP=-1.5" -ar 48000 "$A/v_n.wav"
ffmpeg -v error -y -i "$A/fx.wav" -af "loudnorm=I=-24:TP=-3:LRA=20" -ar 48000 "$A/fx_n.wav"
ffmpeg -v error -y -i "$A/v_n.wav" -i "$A/fx_n.wav" -filter_complex "[0:a]asplit=2[v1][v2];[1:a][v1]sidechaincompress=threshold=0.05:ratio=3:attack=10:release=250[fx];[v2][fx]amix=inputs=2:normalize=0:duration=longest[m]" -map "[m]" "$A/mix.wav"
ffmpeg -v error -y -i "$A/mix.wav" -af "loudnorm=I=-14:TP=-1.0,volume=0.8dB,alimiter=limit=0.89:level=false,apad=whole_dur=$DUR" -t "$DUR" -ar 48000 "$A/mixf.wav"
ffmpeg -v error -y -i "$A/video.mp4" -i "$A/mixf.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -movflags +faststart "$A/reel.mp4"
ffprobe -v error -show_entries stream=codec_type,duration -of compact "$A/reel.mp4"
ffmpeg -i "$A/reel.mp4" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" || true
ls -la "$A/reel.mp4"
