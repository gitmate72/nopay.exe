# 016 BetterWispr — free, open-source voice dictation for Mac (Wispr Flow alt)
# Official site betterwispr.com (read 2026-11-19): "4,301 downloads · Free · macOS 14+ · Apple Silicon recommended",
#   "No account · Local speech models · Meeting notes built in", "Nothing is uploaded", "Free and open source: Apache 2.0".
# Repo github.com/opennookorg/betterwispr (Apache-2.0, 541 stars): "Free, open-source voice dictation for macOS ...
#   Transcription runs on your Mac". Changelog v0.1.6 Nov 13 2026. Listed as a new (Oct 2026) Wispr Flow alternative
#   on saasisdead.si/new. Optional paid extras only if you choose them: your own API key / Claude Code / Codex for
#   "Dictate and format"; core dictation + cleanup run on-device for free.
N = 16
DUR = 32.1
ROLLS = [10.3, 15.6, 20.85, 26.5]
STATUS = [(2.1, 'VOICE TYPING'), (6.4, 'SEARCH'), (10.3, 'DICTATE'), (15.6, 'CLEANUP'), (17.85, 'MEETINGS'),
          (20.85, 'ON-DEVICE'), (23.9, 'PRICE CHECK'), (26.5, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(1.04, 'WISPR FLOW'), until=2.1)
SEARCH = dict(domain='betterwispr.com', t0=6.55, t1=7.6, until=10.3)
FIX = {'Whisper': 'Wispr', 'Whisper.': 'Wispr.', 'betterwhisper': 'betterwispr', 'option': 'Option',
       'space,': 'Space,', 'nopay': 'nopay'}
WINDOWS = [
    (2.1, 6.4, 'fr_home', 2.0, 6.0, ' betterwispr.com '),
    (6.4, 10.3, 'gs', 0, 0, ' google.com '),
    (10.3, 15.6, 'fr_demoz', 3.0, 8.3, ' betterwispr.com / demo '),
    (15.6, 17.85, 'fr_words', 22.0, 23.5, ' betterwispr.com / cleanup '),
    (17.85, 20.85, 'fr_notes', 18.0, 19.6, ' betterwispr.com / meeting notes '),
    (20.85, 23.9, 'fr_local', 18.0, 19.6, ' betterwispr.com / on-device '),
    (23.9, 25.3, 'fr_oss', 24.0, 25.6, ' betterwispr.com / license '),
    (25.3, 26.5, 'fr_free', 4.0, 5.5, ' betterwispr.com '),
]
LABELS = [
    dict(t0=2.25, t1=6.4, kind='inv', text=' VOICE -> TEXT ', x=40, y=110, size=64),
    dict(t0=2.7, t1=6.4, kind='type', text='> works in any app', x=40, y=210, size=56),
    dict(t0=4.7, t1=6.4, kind='inv', text=' BETTERWISPR ', x=40, y=992, size=64),
    dict(t0=8.5, t1=10.3, kind='inv', text=' WISPR = NO "H" ', x=40, y=992, size=60, hit=True),
    dict(t0=10.4, t1=15.6, kind='inv', text=' HOLD ', x=40, y=110, size=64),
    dict(t0=10.6, t1=15.6, kind='inv', text=' OPTION + SPACE ', x=230, y=110, size=64),
    dict(t0=11.75, t1=15.6, kind='type', text='> speak, let go', x=40, y=210, size=56),
    dict(t0=13.1, t1=15.6, kind='inv', text=' CLEAN TEXT LANDS ', x=40, y=992, size=56),
    dict(t0=15.7, t1=17.85, kind='inv', text=' NO MORE "UM" ', x=40, y=110, size=64),
    dict(t0=16.75, t1=17.85, kind='type', text='> learns your words', x=40, y=210, size=56),
    dict(t0=18.0, t1=20.85, kind='inv', text=' MEETING NOTES ', x=40, y=110, size=64),
    dict(t0=19.3, t1=20.85, kind='type', text='> no bot joins', x=40, y=210, size=56),
    dict(t0=21.0, t1=23.9, kind='inv', text=' RUNS ON YOUR MAC ', x=40, y=110, size=64),
    dict(t0=22.6, t1=23.9, kind='type', text='> nothing uploaded', x=40, y=210, size=56),
    dict(t0=24.1, t1=26.5, kind='inv', text=' $0 ', x=40, y=110, size=72, hit=True),
    dict(t0=24.58, t1=26.5, kind='inv', text=' OPEN SOURCE ', x=200, y=110, size=64),
    dict(t0=25.56, t1=26.5, kind='type', text='> no account', x=40, y=210, size=56),
    dict(t0=25.4, t1=26.5, kind='inv', text=' MAC ONLY ', x=40, y=992, size=52),
    dict(t0=26.52, kind='text', text='FREE VOICE TYPING', x=480, y=200, size=76, anchor='ma'),
    dict(t0=26.52, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=26.54, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=27.72, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=28.0, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=28.0, kind='cursor', x=760, y=820, size=132),
    dict(t0=29.14, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
