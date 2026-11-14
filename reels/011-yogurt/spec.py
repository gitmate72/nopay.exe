# 011 Yogurt — free, open-source, private AI meeting notes (Granola alternative) (yogurt.so)
# Official page (yogurt.so FAQ, read 2026-11-14): "Is Yogurt free? Yes. Yogurt is free and open source under the MIT license."
# "After a one-time download of the AI models, transcription and summaries run locally on your computer."
# Mac (Apple silicon, macOS 14.4+), Windows 10 2004+, Ubuntu 22.04+; 8 GB RAM. No bot joins the call.
# Source: Product Hunt daily leaderboard Nov 12 2026 (#16, "Free, private, open-source alternative to Granola"); github.com/FrigadeHQ/yogurt (MIT).
N = 11
DUR = 30.5
ROLLS = [8.1, 20.8, 25.08]
STATUS = [(2.0, 'MEETING NOTES'), (6.2, 'SEARCH'), (8.1, 'NO BOT'), (10.4, 'FEATURES'), (17.4, 'LOCAL AI'),
          (20.8, 'PRICE CHECK'), (25.08, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(0.76, 'GRANOLA'), until=2.0)
SEARCH = dict(domain='yogurt.so', t0=6.3, t1=7.15, until=8.1)
FIX = {'granola.': 'Granola.', '.so.': '.so', 'yogurt': 'yogurt', 'Miss': 'Missed', 'from': 'for', '.exe': '.exe'}
WINDOWS = [
    (2.0, 6.2, 'fr_home', 2.6, 6.8, ' yogurt.so '),
    (6.2, 8.1, 'gs', 0, 0, ' google.com '),
    (8.1, 10.4, 'fr_home', 20.2, 21.4, ' yogurt.so '),
    (10.4, 15.4, 'fr_home', 13.0, 17.6, ' yogurt.so '),
    (15.4, 17.4, 'fr_home', 18.0, 19.4, ' yogurt.so '),
    (17.4, 20.8, 'fr_home', 22.0, 23.6, ' yogurt.so '),
    (20.8, 23.0, 'fr_gh', 4.0, 6.0, ' github.com/FrigadeHQ/yogurt '),
    (23.0, 25.08, 'fr_gh', 17.0, 18.6, ' github.com/FrigadeHQ/yogurt '),
]
LABELS = [
    dict(t0=2.2, t1=6.2, kind='inv', text=' AI MEETING NOTES ', x=40, y=110, size=64),
    dict(t0=3.12, t1=6.2, kind='type', text='> free + open source', x=40, y=210, size=56),
    dict(t0=5.34, t1=6.2, kind='inv', text=' YOGURT ', x=40, y=992, size=64),
    dict(t0=8.24, t1=10.4, kind='inv', text=' NEVER JOINS THE CALL ', x=40, y=110, size=60),
    dict(t0=9.68, t1=10.4, kind='type', text='> no bot', x=40, y=210, size=60),
    dict(t0=10.46, t1=15.4, kind='inv', text=' MIC + COMPUTER AUDIO ', x=40, y=110, size=60),
    dict(t0=12.44, t1=15.4, kind='type', text='> one clear set of notes', x=40, y=210, size=52),
    dict(t0=15.42, t1=17.4, kind='inv', text=' ASK WHAT YOU MISSED ', x=40, y=110, size=62),
    dict(t0=17.52, t1=20.8, kind='inv', text=' AI RUNS ON YOUR PC ', x=40, y=110, size=64),
    dict(t0=19.26, t1=20.8, kind='type', text='> nothing uploaded', x=40, y=210, size=56),
    dict(t0=21.82, t1=25.08, kind='inv', text=' $0 FREE ', x=40, y=110, size=72, hit=True),
    dict(t0=22.28, t1=25.08, kind='type', text='> open source (MIT)', x=40, y=210, size=52),
    dict(t0=23.24, t1=25.08, kind='inv', text=' MAC  WIN  LINUX ', x=40, y=992, size=56),
    dict(t0=25.1, kind='text', text='FREE AI NOTES', x=480, y=200, size=88, anchor='ma'),
    dict(t0=25.1, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=25.12, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=26.0, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=26.32, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=26.32, kind='cursor', x=760, y=820, size=132),
    dict(t0=27.68, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
