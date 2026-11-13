# 010 CuriousLM — private AI that runs on your device, in the browser or on Android (curiouslm.com)
# Official page (curiouslm.com/about + /android, read 2026-11-13): "Free, no account, no ads."
# Source: Product Hunt daily leaderboard Nov 2 2026 (#17); aitoolly.com launch news (Nov 3 2026).
N = 10
DUR = 34.2
ROLLS = [10.0, 24.5, 28.1]
STATUS = [(2.4, 'PRIVATE AI'), (6.9, 'SEARCH'), (10.0, 'ON-DEVICE'), (14.5, 'FEATURES'), (24.5, 'PRICE CHECK'), (28.1, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(1.1, 'PRIVATE AI'), until=2.4)
SEARCH = dict(domain='curiouslm.com', t0=7.1, t1=8.9, until=10.0)
FIX = {'.com.': '.com', 'curiouslm': 'curiouslm', 'price,': 'price?'}
WINDOWS = [
    (2.4, 6.9, 'fr_app', 2.2, 6.6, ' curiouslm.com '),
    (6.9, 10.0, 'gs', 0, 0, ' google.com '),
    (10.0, 14.5, 'fr_app', 14.6, 19.5, ' curiouslm.com '),
    (14.5, 17.9, 'fr_about', 19.2, 21.0, ' curiouslm.com/about '),
    (17.9, 20.9, 'fr_about', 21.6, 24.6, ' curiouslm.com/about '),
    (20.9, 24.5, 'fr_android', 16.9, 17.5, ' curiouslm.com/android '),
    (24.5, 28.1, 'fr_about', 5.0, 9.0, ' curiouslm.com/about '),
]
LABELS = [
    dict(t0=3.14, t1=6.9, kind='type', text='> free, no account', x=40, y=230, size=62),
    dict(t0=5.42, t1=6.9, kind='inv', text=' CURIOUSLM ', x=40, y=110, size=80),
    dict(t0=10.4, t1=14.5, kind='inv', text=' RUNS ON YOUR DEVICE ', x=40, y=110, size=64),
    dict(t0=11.1, t1=14.5, kind='type', text='> right in your browser', x=40, y=210, size=52),
    dict(t0=12.8, t1=14.5, kind='inv', text=' CHATS STAY LOCAL ', x=40, y=992, size=52),
    dict(t0=14.6, t1=17.9, kind='inv', text=' TAP A WORD ', x=40, y=110, size=72),
    dict(t0=15.6, t1=17.9, kind='type', text='> see what it almost said', x=40, y=210, size=52),
    dict(t0=18.68, t1=20.9, kind='inv', text=' VOICE ', x=40, y=110, size=72),
    dict(t0=20.2, t1=20.9, kind='inv', text=' JOURNAL ', x=330, y=110, size=72),
    dict(t0=21.22, t1=24.5, kind='inv', text=' ANDROID ', x=40, y=110, size=72),
    dict(t0=22.34, t1=24.5, kind='type', text='> warns you about scam texts', x=40, y=210, size=48),
    dict(t0=25.62, t1=28.1, kind='inv', text=' $0 FREE ', x=40, y=110, size=72, hit=True),
    dict(t0=26.72, t1=28.1, kind='type', text='> no account', x=40, y=210, size=52),
    dict(t0=27.72, t1=28.1, kind='inv', text=' NO ADS ', x=40, y=992, size=56),
    dict(t0=28.15, kind='text', text='FREE PRIVATE AI', x=480, y=200, size=88, anchor='ma'),
    dict(t0=28.15, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=28.2, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=29.44, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=29.82, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=29.82, kind='cursor', x=760, y=820, size=132),
    dict(t0=31.34, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
