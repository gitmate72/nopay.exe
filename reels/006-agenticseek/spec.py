# 006 AgenticSeek — 100% local Manus alternative (github.com/Fosowl/agenticSeek, GPL-3.0, ~27.6k stars)
N = 6
DUR = 27.6
ROLLS = [8.6, 11.2, 16.5, 22.6]
STATUS = [(2.05, 'AI AGENT'), (8.6, 'SEARCH'), (11.2, 'SKILLS'), (16.5, 'PRIVACY'), (22.6, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(0.9, 'AI AGENTS'), until=2.05)
SEARCH = dict(domain='github.com/Fosowl/agenticSeek', t0=9.1, t1=10.6, until=11.2)
FIX = {'Seek,': 'Seek,', 'from': 'for'}
WINDOWS = [
    (2.05, 8.6, 'fr_site', 1.0, 14.0, ' fosowl.github.io/agenticSeek '),
    (8.6, 11.2, 'gs', 0, 0, ' google.com '),
    (11.2, 16.5, 'fr_site', 18.0, 22.0, ' fosowl.github.io/agenticSeek '),
    (16.55, 19.8, 'fr_site', 22.5, 26.0, ' fosowl.github.io/agenticSeek '),
    (19.8, 22.6, 'fr_gh', 4.0, 7.5, ' github.com/Fosowl/agenticSeek '),
]
LABELS = [
    dict(t0=2.3, t1=8.6, kind='type', text='> runs 100% on your PC', x=40, y=230, size=60),
    dict(t0=4.9, t1=8.6, kind='inv', text=' AGENTICSEEK ', x=40, y=110, size=76),
    dict(t0=7.2, t1=8.6, kind='inv', text=' FREE LOCAL MANUS ALTERNATIVE ', x=40, y=990, size=52),
    dict(t0=11.28, t1=16.5, kind='inv', text=' BROWSES THE WEB ', x=40, y=110, size=56),
    dict(t0=12.66, t1=16.5, kind='inv', text=' WRITES + RUNS CODE ', x=40, y=190, size=56),
    dict(t0=14.22, t1=16.5, kind='inv', text=' PLANS BIG TASKS ', x=40, y=270, size=56),
    dict(t0=15.28, t1=16.5, kind='type', text='> step by step', x=40, y=995, size=60),
    dict(t0=16.6, t1=22.6, kind='inv', text=' NO CLOUD ', x=40, y=110, size=64),
    dict(t0=17.4, t1=22.6, kind='inv', text=' NO DATA SHARING ', x=40, y=200, size=64),
    dict(t0=18.92, t1=22.6, kind='inv', text=' OPEN SOURCE ', x=40, y=290, size=64, hit=True),
    dict(t0=19.9, t1=22.6, kind='type', text='> needs a PC that runs a local model', x=40, y=1000, size=50),
    dict(t0=22.65, kind='text', text='FREE AI AGENT', x=480, y=200, size=92, anchor='ma'),
    dict(t0=22.65, kind='inv', text=' $0 ', x=480, y=340, size=150, anchor='ma'),
    dict(t0=22.7, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=23.25, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=23.58, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=23.58, kind='cursor', x=760, y=820, size=132),
    dict(t0=25.35, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
