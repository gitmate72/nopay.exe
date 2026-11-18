# 015 de:volt — live breadboard circuit simulator in the browser (Proteus alt)
# Official site devoltapp.com (read 2026-11-18), pricing section devoltapp.com/#pricing:
#   "Hobby $0 forever: Live simulation, every part in the catalog; 5 cloud projects, 100 components each;
#    Oscilloscope, multimeter, live readings; SPICE netlist import". Pro A$6.99/mo (AI, analysis workbench, co-editing).
# Guest simulator opens with no sign-in: sim.devoltapp.com/?guest=1. 105 parts, MicroPython on micro:bit V1 / RP2040,
# AVR machine code on UNO R3 / Nano. Source: Product Hunt daily leaderboard Nov 13 2026 ("A breadboard simulator
# with real physics, in your browser"). Paid comparison: Proteus (Labcenter) paid licences.
N = 15
DUR = 30.9
ROLLS = [7.66, 13.74, 19.1, 24.8]
STATUS = [(1.36, 'BREADBOARD'), (5.42, 'SEARCH'), (7.66, 'BUILD'), (10.52, 'LIVE SIM'), (13.74, 'BENCH'),
          (15.78, 'FIRMWARE'), (19.1, 'PRICE CHECK'), (24.8, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(0.72, 'PROTEUS'), until=1.36)
SEARCH = dict(domain='devoltapp.com', t0=5.55, t1=6.75, until=7.66)
FIX = {'Devult.': 'de:volt.', 'devultapp': 'devoltapp', '.com,': '.com.', 'drag': 'Drag', 'hobby': 'Hobby',
       'microbit': 'micro:bit', 'forever.': 'forever:', 'nothing': 'Nothing', 'nopay': 'nopay'}
WINDOWS = [
    (1.36, 5.42, 'fr_home', 2.2, 6.2, ' devoltapp.com '),
    (5.42, 7.66, 'gs', 0, 0, ' google.com '),
    (7.66, 10.52, 'fr_sim2', 13.4, 16.8, ' sim.devoltapp.com '),
    (10.52, 13.74, 'fr_live', 7.0, 10.2, ' devoltapp.com / live circuit '),
    (13.74, 15.78, 'fr_home', 23.2, 25.0, ' devoltapp.com / the bench '),
    (15.78, 19.1, 'fr_home', 25.8, 27.6, ' devoltapp.com / firmware '),
    (19.1, 24.8, 'fr_pricing', 6.0, 13.0, ' devoltapp.com/#pricing '),
]
LABELS = [
    dict(t0=1.6, t1=5.42, kind='inv', text=' BREADBOARD SIMULATOR ', x=40, y=110, size=60),
    dict(t0=2.2, t1=5.42, kind='type', text='> runs in your browser', x=40, y=210, size=54),
    dict(t0=4.4, t1=5.42, kind='inv', text=' DE:VOLT ', x=40, y=992, size=64),
    dict(t0=7.9, t1=10.52, kind='inv', text=' DRAG ', x=40, y=110, size=64),
    dict(t0=8.78, t1=10.52, kind='inv', text=' DROP ', x=250, y=110, size=64),
    dict(t0=9.68, t1=10.52, kind='inv', text=' WIRE ', x=460, y=110, size=64),
    dict(t0=8.4, t1=10.52, kind='type', text='> no sign-up: guest mode', x=40, y=210, size=50),
    dict(t0=10.8, t1=13.74, kind='inv', text=' RUNS LIVE ', x=40, y=110, size=64),
    dict(t0=11.6, t1=13.74, kind='type', text='> 555 clock + counter', x=40, y=210, size=52),
    dict(t0=12.4, t1=13.74, kind='inv', text=' REAL SPICE-STYLE MATH ', x=40, y=992, size=50),
    dict(t0=13.8, t1=15.78, kind='inv', text=' 105 PARTS ', x=40, y=110, size=64),
    dict(t0=14.7, t1=15.78, kind='type', text='> 4-channel scope', x=40, y=210, size=54),
    dict(t0=16.0, t1=19.1, kind='inv', text=' ARDUINO ', x=40, y=110, size=60),
    dict(t0=16.7, t1=19.1, kind='inv', text=' MICRO:BIT ', x=350, y=110, size=60),
    dict(t0=17.6, t1=19.1, kind='type', text='> your code really runs', x=40, y=210, size=52),
    dict(t0=19.98, t1=24.8, kind='inv', text=' $0 FOREVER ', x=40, y=110, size=72, hit=True),
    dict(t0=21.56, t1=24.8, kind='type', text='> every part', x=40, y=210, size=54),
    dict(t0=22.56, t1=24.8, kind='type', text='> 5 cloud projects', x=40, y=290, size=54),
    dict(t0=23.86, t1=24.8, kind='inv', text=' NO INSTALL ', x=40, y=992, size=60),
    dict(t0=24.82, kind='text', text='FREE CIRCUIT LAB', x=480, y=200, size=80, anchor='ma'),
    dict(t0=24.82, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=24.84, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=25.96, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=26.38, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=26.38, kind='cursor', x=760, y=820, size=132),
    dict(t0=27.76, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
