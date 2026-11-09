# nopay.exe

Automation for the Instagram page **@nopay.exe**: free AI tools and offers, one reel at a time, in a green CRT terminal style.

## How it runs
1. **Every morning** a scheduled Claude session follows `CLAUDE.md`: finds 1 new tool with a real free plan, records their real websites, makes the voiceover, renders 1 reel and puts them in the queue: the `queue` branch, one folder per reel (`reel.mp4` + `caption.txt`).
2. **Once a day, at a random US prime-time minute** (12–2 pm or 6–9 pm ET) the `Post reel to Instagram` workflow publishes the oldest queued reel and logs it in `posted/log.md`.

## Stop a reel
Switch to the **queue** branch on GitHub, open the reel's folder and delete it (delete `reel.mp4`) before its time. It will not be posted.

## Secrets (Settings → Secrets and variables → Actions)
| Name | What |
|---|---|
| `IG_ACCESS_TOKEN` | Instagram long-lived access token (Instagram API with Instagram Login, `instagram_business_content_publish`) |
| `IG_USER_ID` | Instagram professional account user ID |
| `GH_PAT` (optional) | Fine-grained GitHub token for this repo with *Secrets: read and write*, so the token refresh can save the new token |

Test without posting: Actions → *Post reel to Instagram* → Run workflow (dry run is on by default).
The oldest folder on `queue` is posted next; after posting the folder is removed and the branch history is squashed so videos don't pile up.
