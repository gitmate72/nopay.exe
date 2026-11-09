# nopay.exe — daily reel factory

Instagram page **@nopay.exe**: English, faceless, one reel = one NEW free tool/offer, in the green CMD/CRT "Phosphor Terminal" look.
This repo holds the whole pipeline. A scheduled session runs the **Daily run** below every morning and queues 1 reel;
GitHub Actions posts **1 reel per day** (oldest first) at a random US prime-time minute (12–2 pm or 6–9 pm US Eastern) from the `queue` branch. Audience: USA.

## Hard rules (from the owner — do not change)
1. **Voice:** ElevenLabs **Marcus – Bright, Upbeat and Clear** (`voice_id y0s2ExEMuum3muUnA6Zd`), model `eleven_v3`, **`generations_count: 1` — always ONE take** (credits). Never regenerate to "retry". If speech can't be generated, stop and report.
2. **Topic:** only **NEW / trending** tools and **new free offers** (AI agents, AI browsers, new AI tools with a real free plan, new free courses/certificates, new student/creator freebies). No old, well-known tools (e.g. iLovePDF, Photopea, Canva). Check `posted/log.md` and `topics.md` so a tool is never repeated.
3. **Free must be true:** read the tool's **official pricing page** the same day. No card, no trial-only. If the exact free limit can't be confirmed, say only "start free" with no number. If the headline feature is paid, pick another tool. Never piracy/cracks.
4. **Real screen recording in every reel:** record the real site with `pipeline/record/capture_site.js` (public pages only, never log in). If nothing usable can be recorded (blocked, login wall, blank), choose another tool.
5. **Google search with the FULL domain**, typed and zoomed: `pipeline/record/google_typing.js <domain>`; the URL is also typed big in VT323 above the window with an arrow into the box; the voiceover says the domain ("zcad dot A I").
6. **Look:** green CRT terminal; **website footage inside the window stays in ORIGINAL COLOURS** (never green-tinted). Use `reels/003-zcad/reel.py` as the template (it has `crt_color`).
7. **Safe zone:** nothing important below output y=1440 or in the right 230 px. Subtitles: buffer y=1150, centred x=400, max width 700, spoken word in inverse video, auto-shrink so they are never cut.
8. Length 25–35 s. Hook in the first 2 s. End: "Save this, and follow nopay dot exe for more free AI."

## Daily run (scheduled session)
Work in this repo. Make **1 reel**. Queue folder name = next free day after the newest queued folder, e.g. `<YYYYMMDD>-1200` (the name only sets the order; the real posting time is random US prime time).
0. `bash pipeline/setup.sh`. Read `posted/log.md`, `topics.md`, list the queue: `git ls-remote --heads origin queue && git fetch -q --depth 1 origin queue && git ls-tree --name-only origin/queue`. If 3+ reels are already queued, make none and stop.
1. **Research** (WebSearch/WebFetch, sources ≤30 days old): "new AI tool free <month year>", "now free", "free plan launched", agent/browser roundups. Shortlist 3, check each official pricing page (Playwright text dump if WebFetch fails), drop paid/trial/old/repeated ones, pick 1. Note the source URLs.
2. **Script** per reel (~30 s, ~75–90 words): hook → name + "search <domain>" → 2–3 things it does (that the footage can show) → the free plan in exact words from the pricing page → CTA. Write 3–4 hooks, score with `python3 pipeline/tools/ig-reel/hookscore.py hooks.txt`, take the best (≥75; brand-fit "Stop paying for …" is good).
3. **Voice:** ElevenLabs `creative_generate_speech` (rule 1). Download the mp3 from the returned content_url, then `bash pipeline/audio/tighten.sh voice.mp3 reels/NNN-slug/assets` (writes vo.wav + words.json).
4. **Record:** `node pipeline/record/capture_site.js reels/NNN-slug/assets name=url ...` (home, product/demo, pricing), extract frames `ffmpeg -i assets/vid_<name>/*.webm -vf fps=30 -q:v 3 assets/fr_<name>/%04d.jpg`, and `node pipeline/record/google_typing.js <domain> reels/NNN-slug/assets/gs`. Make a timestamped contact sheet and pick footage times that skip blank loading seconds and cookie banners.
5. **Build:** write `reels/NNN-slug/spec.py` (copy `reels/008-inboxzero/spec.py`: N, DUR, ROLLS, STATUS, HOOK, SEARCH{domain,t0,t1 so typing ends on the spoken domain}, WINDOWS of real footage, LABELS, FIX for whisper typos). The shared engine is `reels/_lib/specreel.py` (subtitles come from words.json) and sfx are automatic (`reels/_lib/autosfx.py`). Check frames with `python3 reels/_lib/specreel.py reels/NNN-slug check <t> ...` and LOOK at them (labels overlapping, cut text, empty window). Then `bash pipeline/build.sh reels/NNN-slug <duration> 2` (duration = voice + 1 s; 2 workers, ~10+ min). Verify audio duration = video duration and ~-14 LUFS.
5b. **Cover:** `python3 pipeline/cover.py <best real footage frame> reels/NNN-slug/assets/cover.jpg <N> <PAID TOOL> <domain> ' $0 <WHAT> ' '<fact · fact>' '<fact · fact>'` and LOOK at it (no half-loaded/white frames). queue_reel.sh copies it; it is posted as the reel cover.
6. **Caption** → `reels/NNN-slug/caption.txt`: hook line, 2–4 short lines (domain, free plan in plain words, limits), one ask, "Follow @nopay.exe for free AI daily.", 3 hashtags.
7. **Queue:** `bash scripts/queue_reel.sh reels/NNN-slug <YYYYMMDD-HHMM> <slug>` (pushes the video to the `queue` branch; GitHub Releases are not allowed from Claude sessions); add the tool to `topics.md` (date, tool, domain, free claim, pricing URL). Commit `reels/NNN-slug/{spec.py,caption.txt}` + topics.md (never assets/) and push to main.
8. Finish with a short report: the tool, hooks + scores, free claims with sources, queue folders, and anything skipped and why.

## Layout
- `pipeline/engine/` CRT engine + fonts (VT323, Space Mono; OFL)
- `pipeline/record/` Playwright recording + Google typing
- `pipeline/audio/` tighten + word timestamps (faster-whisper)
- `pipeline/tools/ig-reel/` hook scorer (MIT, from Jakeschincariol/instagram-agent-skill)
- `reels/NNN-slug/` per-reel script, sfx, caption (assets/ is git-ignored)
- `scripts/` queue (branch `queue`, one folder per reel) + Instagram posting; `.github/workflows/` posting schedule + token refresh
- `posted/log.md` what went live; `topics.md` every tool used
