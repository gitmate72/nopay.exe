# 004 Concat — free, open-source video editor (concat.standalones.org, github.com/jub0t/Concat, AGPL-3.0)
N = 4
DUR = 27.0
ROLLS = [8.45, 16.25, 21.7]
STATUS = [(1.75, 'VIDEO EDITOR'), (5.6, 'SEARCH'), (8.45, 'FEATURES'), (16.25, 'CATCHES: 0'), (21.7, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(0.82, 'CAPCUT PRO'), until=1.75)
SEARCH = dict(domain='concat.standalones.org', t0=5.95, t1=7.9, until=8.45)
FIX = {'Kincat.': 'Concat.', 'kincat.standalones.org.': 'concat.standalones.org', 'kincat': 'concat'}
WINDOWS = [
    (1.75, 5.6, 'fr_home', 2.0, 6.0, ' concat.standalones.org '),
    (5.6, 8.45, 'gs', 0, 0, ' google.com '),
    (8.45, 12.0, 'fr_home', 14.0, 16.6, ' concat.standalones.org '),
    (12.0, 16.25, 'fr_home', 21.0, 26.0, ' concat.standalones.org '),
    (16.3, 21.7, 'fr_home', 17.0, 19.6, ' concat.standalones.org '),
]
LABELS = [
    dict(t0=2.65, t1=5.6, kind='type', text='> free + open source', x=40, y=230, size=62),
    dict(t0=4.7, t1=5.6, kind='inv', text=' CONCAT ', x=40, y=110, size=96),
    dict(t0=9.0, t1=16.25, kind='inv', text=' MAC ', x=40, y=110, size=56),
    dict(t0=9.5, t1=16.25, kind='inv', text=' WINDOWS ', x=200, y=110, size=56),
    dict(t0=10.0, t1=16.25, kind='inv', text=' LINUX ', x=470, y=110, size=56),
    dict(t0=10.6, t1=16.25, kind='inv', text=' ANDROID ', x=680, y=110, size=56),
    dict(t0=8.6, t1=16.25, kind='type', text='> runs on', x=40, y=220, size=56),
    dict(t0=11.95, t1=16.25, kind='type', text='+ auto-captions', x=40, y=990, size=52),
    dict(t0=12.65, t1=16.25, kind='type', text='+ text-to-speech', x=480, y=990, size=52),
    dict(t0=13.6, t1=16.25, kind='type', text='+ bg removal', x=40, y=1052, size=52),
    dict(t0=14.8, t1=16.25, kind='inv', text=' 4K EXPORT ', x=480, y=1050, size=52),
    dict(t0=16.42, t1=21.7, kind='inv', text=' NO WATERMARK ', x=40, y=110, size=64),
    dict(t0=17.34, t1=21.7, kind='inv', text=' NO ACCOUNT ', x=40, y=200, size=64),
    dict(t0=18.38, t1=21.7, kind='inv', text=' NO SUBSCRIPTION ', x=40, y=290, size=64, hit=True),
    dict(t0=19.7, t1=21.7, kind='type', text='> footage stays on your PC', x=40, y=1000, size=56),
    dict(t0=21.75, kind='text', text='FREE VIDEO EDITOR', x=480, y=200, size=92, anchor='ma'),
    dict(t0=21.75, kind='inv', text=' $0 ', x=480, y=340, size=150, anchor='ma'),
    dict(t0=21.86, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=22.5, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=22.82, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=22.82, kind='cursor', x=760, y=820, size=132),
    dict(t0=24.8, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
