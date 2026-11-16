# 013 CaptureFlow — open-source screen recorder with instant share links (Loom alternative), captureflow.dev
# Pricing page (captureflow.dev/pricing, read 2026-11-16): "Start free." Free = $0, "Up to 25" recordings per person,
# "5 min per video", transcripts/captions/AI chapters included; "Free download. No credit card." "You can also self-host
# CaptureFlow for free." Open source under the AGPL (github.com/sardorml/captureflow). Light $5/mo, Pro $12/mo.
# Source: Product Hunt daily leaderboard Nov 14 2026 ("Open-source screen recorder with instant share links").
N = 13
DUR = 30.9
ROLLS = [7.6, 18.18, 25.38]
STATUS = [(1.86, 'SCREEN REC'), (5.46, 'SEARCH'), (7.6, 'RECORD'), (11.22, 'AI NOTES'), (14.44, 'AI AGENT'),
          (18.18, 'PRICE CHECK'), (25.38, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(1.02, 'LOOM'), until=1.86)
SEARCH = dict(domain='captureflow.dev', t0=5.6, t1=6.85, until=7.6)
FIX = {'Capture': 'Capture', 'Flow,': 'Flow,', 'loom.': 'Loom.', 'chatgbt': 'ChatGPT', 'captureflow': 'captureflow',
       '.dev.': '.dev', 'notepay': 'nopay', '-host': '-host'}
WINDOWS = [
    (1.86, 5.46, 'fr_home', 1.5, 5.0, ' captureflow.dev '),
    (5.46, 7.6, 'gs', 0, 0, ' google.com '),
    (7.6, 11.22, 'fr_home', 18.0, 21.6, ' captureflow.dev '),
    (11.22, 14.44, 'fr_features', 20.0, 23.0, ' captureflow.dev/features '),
    (14.44, 18.18, 'fr_home', 22.0, 26.0, ' captureflow.dev '),
    (18.18, 23.84, 'fr_pricing', 1.0, 12.5, ' captureflow.dev/pricing '),
    (23.84, 25.38, 'fr_pricing', 14.0, 15.6, ' captureflow.dev/pricing '),
]
LABELS = [
    dict(t0=2.5, t1=5.46, kind='inv', text=' SCREEN RECORDER ', x=40, y=110, size=64),
    dict(t0=3.72, t1=5.46, kind='type', text='> free + open source', x=40, y=210, size=56),
    dict(t0=2.6, t1=5.46, kind='inv', text=' CAPTUREFLOW ', x=40, y=992, size=64),
    dict(t0=8.44, t1=11.22, kind='inv', text=' CHROME EXTENSION ', x=40, y=110, size=64),
    dict(t0=9.28, t1=11.22, kind='type', text='> link ready on stop', x=40, y=210, size=56),
    dict(t0=11.76, t1=14.44, kind='inv', text=' TRANSCRIPT ', x=40, y=110, size=60),
    dict(t0=12.34, t1=14.44, kind='inv', text=' CHAPTERS ', x=440, y=110, size=60),
    dict(t0=13.32, t1=14.44, kind='inv', text=' AI TITLE ', x=40, y=992, size=60),
    dict(t0=15.1, t1=18.18, kind='inv', text=' AI RECORDS FOR YOU ', x=40, y=110, size=60),
    dict(t0=15.78, t1=18.18, kind='type', text='> Claude / ChatGPT / Cursor', x=40, y=210, size=46),
    dict(t0=18.96, t1=25.38, kind='inv', text=' $0 FREE ', x=40, y=110, size=72, hit=True),
    dict(t0=20.26, t1=25.38, kind='type', text='> 25 recordings', x=40, y=210, size=52),
    dict(t0=21.72, t1=25.38, kind='type', text='> 5 min each', x=40, y=290, size=52),
    dict(t0=22.62, t1=23.84, kind='inv', text=' NO CREDIT CARD ', x=40, y=992, size=56),
    dict(t0=23.84, t1=25.38, kind='inv', text=' OR SELF-HOST FREE ', x=40, y=992, size=56),
    dict(t0=25.42, kind='text', text='FREE LOOM ALT', x=480, y=200, size=80, anchor='ma'),
    dict(t0=25.42, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=25.44, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=26.62, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=26.88, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=26.88, kind='cursor', x=760, y=820, size=132),
    dict(t0=28.14, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
