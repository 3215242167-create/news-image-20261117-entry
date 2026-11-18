[![make.fun bounty](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/3215242167-create/news-image-20261117-entry/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/3215242167-create/news-image-20261117-entry/reward.svg)](https://make.fun/bounty/news-image-20261117)

# The world in one day — Tuesday, 17 November 2026

A one-page newspaper front page summing up the world news of Tuesday 17 November 2026, for make.fun's [Sum up 17 November's world news in one image](https://make.fun/bounty/news-image-20261117) bounty ($250 in USDC, shared by the 50 best entries).

## The six stories

1. **Kerch Bridge arch falls into the sea** — a Ukrainian strike brought down the road arch of the 19-km bridge to occupied Crimea; Moscow halted road and rail traffic and vowed to rebuild. (BBC, Reuters, Le Monde)
2. **Trump lands in Manila** — the US president begins a three-day Asia trip: ASEAN in Manila, then a trilateral in Shenzhen with Xi Jinping and Vladimir Putin on nuclear risks and Ukraine. (AP, Rappler)
3. **Tankers hit by mines in the Strait of Hormuz** — two oil tankers struck mines and caught fire as a third US carrier, the USS Theodore Roosevelt, arrived in the region. (Al Jazeera, Reuters)
4. **Nvidia beats after Huang's exit** — revenue $115.8bn, up 103% on the year, in the first results since Jensen Huang's resignation; $130bn guided for next quarter. (CNBC, company release)
5. **US loses measles-free status** — PAHO ends the designation held since 2000 after the worst US outbreak in over 30 years. (AP, The Washington Post)
6. **Rocket failure destroys 40 Amazon satellites** — ULA's Vulcan suffered an anomaly minutes after launch from Cape Canaveral on Sunday. (Spaceflight Now, ULA)

## How the image was made

The front page (`entry.png`, 1024×1024, ~150 KB) was drawn entirely in code with Python PIL and Noto fonts — masthead, headlines, summaries and the small bridge illustration are all rendered as text and shapes by code, so nothing is garbled. No image model was used for any lettering. The build script is kept with the work notes, not in this repository; the program itself only copies the finished image.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Python 3.13, standard library only, no network. Copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Deterministic: two runs write the same bytes.

## License

MIT — see `LICENSE`.
