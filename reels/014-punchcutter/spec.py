# 014 Punchcutter — open-source AI type foundry: handwriting photo or one sentence -> real font family (Calligraphr alt)
# Official site byrishi.github.io/punchcutter (read 2026-11-17): footer "MIT license"; README: "Code: MIT. Fonts you make
# are yours, under whatever license you choose." No paid plan, no pricing. Runs inside Claude / ChatGPT / Codex / MCP
# clients, or a plain CLI ("No AI at all"). Repo github.com/byrishi/punchcutter (v1.3.1, files committed 2 days ago).
# Source: Product Hunt daily leaderboard Nov 16 2026 ("Turn a sentence or your handwriting into a real font family").
# Paid comparison: calligraphr.com/en/pricing — Pro $10 for one month (free plan 75 characters/font).
N = 14
DUR = 34.6
ROLLS = [8.92, 17.52, 28.18]
STATUS = [(1.66, 'FONT LAB'), (4.86, 'SEARCH'), (8.92, 'HANDWRITING'), (14.56, 'PROMPT'), (17.52, 'STUDIO'),
          (22.06, 'AGENTS'), (25.14, 'LICENSE'), (28.18, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(0.74, 'CALLIGRAPHR'), until=1.66)
SEARCH = dict(domain='byrishi.github.io/punchcutter', t0=5.0, t1=7.94, until=8.92)
FIX = {'calligrapher.': 'Calligraphr.', 'Punch': 'Punch', 'Cutter.': 'cutter.', 'by': 'by',
       '.github': '.github', '.io': '.io', 'studio.': 'Studio:', 'Chat': 'Chat', 'nopay': 'nopay'}
WINDOWS = [
    (1.66, 4.86, 'fr_home', 2.0, 5.2, ' byrishi.github.io/punchcutter '),
    (4.86, 8.92, 'gs', 0, 0, ' google.com '),
    (8.92, 11.52, 'fr_home', 22.0, 24.6, ' punchcutter / handwriting '),
    (11.52, 14.56, 'fr_home', 23.8, 26.84, ' punchcutter / handwriting '),
    (14.56, 17.52, 'fr_home', 16.4, 19.36, ' punchcutter / six ways in '),
    (17.52, 19.62, 'fr_studio', 2.0, 4.1, ' punchcutter studio '),
    (19.62, 22.06, 'fr_studio', 13.6, 16.04, ' punchcutter studio '),
    (22.06, 25.14, 'fr_gh', 19.5, 22.58, ' github.com/byrishi/punchcutter '),
    (25.14, 28.18, 'fr_gh', 7.0, 10.04, ' github.com/byrishi/punchcutter '),
]
LABELS = [
    dict(t0=2.2, t1=4.86, kind='inv', text=' HANDWRITING -> FONT ', x=40, y=110, size=60),
    dict(t0=3.0, t1=4.86, kind='type', text='> free + open source', x=40, y=210, size=56),
    dict(t0=3.7, t1=4.86, kind='inv', text=' PUNCHCUTTER ', x=40, y=992, size=64),
    dict(t0=9.2, t1=11.52, kind='inv', text=' ANY PAPER ', x=40, y=110, size=64),
    dict(t0=10.76, t1=11.52, kind='type', text='> snap a photo', x=40, y=210, size=56),
    dict(t0=11.74, t1=14.56, kind='inv', text=' TRACES EVERY LETTER ', x=40, y=110, size=60),
    dict(t0=12.9, t1=14.56, kind='type', text='> spacing + kerning', x=40, y=210, size=50),
    dict(t0=13.46, t1=14.56, kind='inv', text=' REAL FONT FAMILY ', x=40, y=992, size=56),
    dict(t0=14.8, t1=17.52, kind='inv', text=' OR: 1 SENTENCE ', x=40, y=110, size=64),
    dict(t0=15.66, t1=17.52, kind='type', text='> "soft, friendly, rounded"', x=40, y=210, size=46),
    dict(t0=17.74, t1=22.06, kind='inv', text=' OWN STUDIO APP ', x=40, y=110, size=64),
    dict(t0=19.62, t1=22.06, kind='type', text='> weight slider', x=40, y=210, size=52),
    dict(t0=20.42, t1=22.06, kind='type', text='> type tester', x=40, y=290, size=52),
    dict(t0=21.2, t1=22.06, kind='inv', text=' TTF / OTF / WOFF2 ', x=40, y=992, size=56),
    dict(t0=22.4, t1=25.14, kind='inv', text=' CLAUDE ', x=40, y=110, size=60),
    dict(t0=23.44, t1=25.14, kind='inv', text=' CHATGPT ', x=330, y=110, size=60),
    dict(t0=24.4, t1=25.14, kind='inv', text=' CODEX ', x=660, y=110, size=60),
    dict(t0=25.66, t1=28.18, kind='inv', text=' $0 FREE ', x=40, y=110, size=72, hit=True),
    dict(t0=26.14, t1=28.18, kind='type', text='> open source', x=40, y=210, size=52),
    dict(t0=27.22, t1=28.18, kind='inv', text=' MIT LICENSE ', x=40, y=992, size=60),
    dict(t0=28.2, kind='text', text='FREE FONT MAKER', x=480, y=200, size=80, anchor='ma'),
    dict(t0=28.2, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=28.22, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=29.38, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=29.72, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=29.72, kind='cursor', x=760, y=820, size=132),
    dict(t0=31.58, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
