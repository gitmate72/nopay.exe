# 005 VoiceStudio — local, open-source AI voice studio (voicestudio.sh, github.com/debpalash/VoiceStudio, AGPL-3.0, 105k stars)
N = 5
DUR = 28.0
ROLLS = [8.5, 13.95, 22.8]
STATUS = [(1.95, 'VOICE STUDIO'), (6.5, 'SEARCH'), (8.5, 'FEATURES'), (13.95, 'GITHUB'), (22.8, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(0.9, 'ELEVENLABS'), until=1.95)
SEARCH = dict(domain='voicestudio.sh', t0=6.75, t1=7.9, until=8.5)
FIX = {'11Labs.': 'ElevenLabs.', 'Studio.': 'Studio.', 'voicestudio.sh,': 'voicestudio.sh'}
WINDOWS = [
    (1.95, 6.5, 'fr_home', 2.0, 6.5, ' voicestudio.sh '),
    (6.5, 8.5, 'gs', 0, 0, ' google.com '),
    (8.5, 13.95, 'fr_home', 16.0, 21.5, ' voicestudio.sh '),
    (13.95, 17.2, 'fr_gh', 9.5, 12.5, ' github.com/debpalash/VoiceStudio '),
    (17.2, 22.8, 'fr_home', 22.0, 24.6, ' voicestudio.sh '),
]
LABELS = [
    dict(t0=2.6, t1=6.5, kind='type', text='> runs on your laptop', x=40, y=230, size=60),
    dict(t0=3.05, t1=6.5, kind='inv', text=' FREE ', x='right', y=110, size=72),
    dict(t0=5.5, t1=6.5, kind='inv', text=' VOICESTUDIO ', x=40, y=110, size=72),
    dict(t0=8.96, t1=13.95, kind='inv', text=' CLONE ', x=40, y=110, size=56),
    dict(t0=9.56, t1=13.95, kind='inv', text=' DUB ', x=250, y=110, size=56),
    dict(t0=10.4, t1=13.95, kind='inv', text=' TRANSCRIBE ', x=410, y=110, size=56),
    dict(t0=11.12, t1=13.95, kind='inv', text=' NARRATE ', x=40, y=200, size=56),
    dict(t0=11.78, t1=13.95, kind='count', to=646, t_end=13.0, suffix=' LANGUAGES', x=40, y=995, size=84),
    dict(t0=14.4, t1=22.8, kind='count', to=100000, step=1000, t_end=15.4, suffix='+ STARS', x=40, y=110, size=84, hit=True),
    dict(t0=17.7, t1=22.8, kind='inv', text=' OPEN SOURCE ', x=40, y=990, size=56),
    dict(t0=18.68, t1=22.8, kind='inv', text=' FREE ON YOUR DEVICE ', x=40, y=1052, size=52),
    dict(t0=20.7, t1=22.8, kind='type', text='> pro + cloud: optional', x=40, y=230, size=56),
    dict(t0=22.85, kind='text', text='FREE VOICE STUDIO', x=480, y=200, size=92, anchor='ma'),
    dict(t0=22.85, kind='inv', text=' $0 ', x=480, y=340, size=150, anchor='ma'),
    dict(t0=22.9, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=23.55, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=23.9, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=23.9, kind='cursor', x=760, y=820, size=132),
    dict(t0=25.75, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
