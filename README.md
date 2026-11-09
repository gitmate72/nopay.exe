# nopay.exe

Automation for the Instagram page **@nopay.exe**: free AI tools and offers, one reel at a time, in a green CRT terminal style.

## How it runs
1. **Every morning** a scheduled Claude session follows `CLAUDE.md`: finds 2 new tools with a real free plan, records their real websites, makes the voiceover, renders 2 reels and puts them in the queue (GitHub Releases named `queue-…`).
2. **13:00 and 19:30 IST** the `Post reel to Instagram` workflow publishes the oldest queued reel and logs it in `posted/log.md`.

## Stop a reel
Open **Releases**, delete the `queue-…` release before its time. It will not be posted.

## Secrets (Settings → Secrets and variables → Actions)
| Name | What |
|---|---|
| `IG_ACCESS_TOKEN` | Instagram long-lived access token (Instagram API with Instagram Login, `instagram_business_content_publish`) |
| `IG_USER_ID` | Instagram professional account user ID |
| `GH_PAT` (optional) | Fine-grained GitHub token for this repo with *Secrets: read and write*, so the token refresh can save the new token |

Test without posting: Actions → *Post reel to Instagram* → Run workflow (dry run is on by default).
