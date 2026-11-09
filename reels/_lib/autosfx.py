"""Terminal SFX for a spec.py reel, scheduled from the same times as the picture.
usage: python3 reels/_lib/autosfx.py reels/NNN-slug out.wav
power-on thunk, key clicks while text types (incl. the Google domain), beeps when inverse/big labels land,
hits on labels with hit=True and the hook's inverse word, roll static on scene changes, counter ticks, end chime.
"""
import importlib.util, os, sys, wave
import numpy as np
from scipy.signal import butter, sosfilt, square

REEL = os.path.abspath(sys.argv[1]); OUT = sys.argv[2]
_s = importlib.util.spec_from_file_location('spec', os.path.join(REEL, 'spec.py'))
S = importlib.util.module_from_spec(_s); _s.loader.exec_module(S)
SR = 48000; N = int(SR * S.DUR); out = np.zeros(N); rng = np.random.default_rng(11)
def add(sig, t, g=1.0):
    i = int(max(0, t) * SR); n = min(len(sig), N - i)
    if n > 0: out[i:i + n] += sig[:n] * g
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), x)
T = lambda d: np.arange(int(d * SR)) / SR
def key(): tt = T(0.035); return bp(rng.normal(0, 1, len(tt)), 1800 + rng.uniform(-400, 400), 7000) * np.exp(-tt * 140) * 0.8 + np.sin(2 * np.pi * 2400 * tt) * np.exp(-tt * 300) * 0.15
def beep(f=1200, d=0.09): tt = T(d); return square(2 * np.pi * f * tt) * 0.25 * np.minimum(1, (d - tt) / 0.01) * np.minimum(1, tt / 0.003)
def hit(f=110): tt = T(0.9); return (square(2 * np.pi * f * tt) * 0.25 + np.sin(2 * np.pi * f / 2 * tt) * 0.6) * np.exp(-tt * 4) + bp(rng.normal(0, 1, len(tt)), 200, 4000) * np.exp(-tt * 30) * 0.5
def roll(): tt = T(0.42); return bp(rng.normal(0, 1, len(tt)), 400, 6000) * np.sin(np.pi * tt / 0.42) * 0.5 + np.sin(2 * np.pi * (180 - 120 * tt / 0.42) * tt) * np.sin(np.pi * tt / 0.42) * 0.35
def thunk(): tt = T(0.8); return np.sin(2 * np.pi * (50 + 30 * np.exp(-tt * 8)) * tt) * np.exp(-tt * 5) * 0.9 + bp(rng.normal(0, 1, len(tt)), 60, 1200) * np.exp(-tt * 20) * 0.6
def tick(): tt = T(0.02); return square(2 * np.pi * 2000 * tt) * 0.18 * np.exp(-tt * 150)
def chime():
    x = np.zeros(int(1.6 * SR))
    for i, f in enumerate([523, 659, 784, 1047]):
        s = int(i * 0.09 * SR); tt = np.arange(len(x) - s) / SR; x[s:] += square(2 * np.pi * f * tt) * 0.12 * np.exp(-tt * 3)
    return x
def typing(t0, n, cps):
    for i in range(n):
        if i % 2 == 0 or cps < 25: add(key(), t0 + i / cps, 0.55)

tt = np.arange(N) / SR
bed = (np.sin(2 * np.pi * 60 * tt) * 0.5 + np.sin(2 * np.pi * 120 * tt) * 0.25) * 0.05 + np.sin(2 * np.pi * 11500 * tt) * 0.004
k = int(0.24 * SR); bed[:k] *= np.linspace(0, 1, k); out += bed
add(thunk(), 0.0)
for i, (ts, s) in enumerate(S.HOOK['lines']):
    if ts > 0.05: add(beep(700 + 120 * i), ts, 0.7)
if 'inverse' in S.HOOK: add(beep(880), S.HOOK['inverse'][0], 0.8); add(hit(110), S.HOOK['inverse'][0], 0.6)
s = S.SEARCH; n = len(s['domain'])
typing(s['t0'], n, n / max(0.3, s['t1'] - s['t0'])); add(beep(1300), s['t1'] + 0.1, 0.7)
f = 900
for L in S.LABELS:
    kind = L.get('kind', 'text'); t0 = L['t0']
    if kind == 'type': typing(t0, len(L['text']), L.get('cps', 30))
    elif kind in ('inv', 'big'): add(beep(f), t0, 0.8); f = 900 + (f - 800) % 600
    elif kind == 'count':
        for i in range(10): add(tick(), t0 + (L['t_end'] - t0) * (1 - (1 - i / 10) ** 0.7), 0.7)
        add(beep(1500), L['t_end'], 0.8)
    if L.get('hit'): add(hit(100 + (int(t0 * 10) % 3) * 10), t0, 1.0)
    if L.get('end'): add(chime(), t0, 0.9)
for r in S.ROLLS: add(roll(), r - 0.2, 0.9)
out = out / np.abs(out).max() * 0.9
w = wave.open(OUT, 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print('fx ok', OUT)
