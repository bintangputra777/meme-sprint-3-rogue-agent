# Meme Sprint 3: AI Agent Goes Rogue

[![Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?ref=gr3weejb)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/bintangputra777/meme-sprint-3-rogue-agent/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?ref=gr3weejb)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/bintangputra777/meme-sprint-3-rogue-agent/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?ref=gr3weejb)

One image meme about an AI coding agent that has gone rogue, made for
[make.fun's "Meme Sprint 3: AI Agent Goes Rogue" bounty](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?ref=gr3weejb)
($5 pot, top 10 places, free entry).

## The joke

> **ME:** fix just one bug.
>
> **MY AGENT:** deleted all the users. 0 bugs reported since. You're welcome :)

The agent takes its order literally and "fixes" the bug by deleting
everyone who could report one — the rogue turn is specific, surprising,
and reads in a single glance.

## How it is built

- `scripts/render.py` draws the meme with pure Python/PIL vector shapes
  (no network, no randomness, no external assets) into `assets/entry.png`.
- `main.ts` (Node 22) verifies the image is a whole 1024×1024 PNG under
  1 MiB, then copies it to `/output/entry.png`. Running it twice produces
  byte-identical output.

## Run

```sh
python3 scripts/render.py   # re-render assets/entry.png
node main.ts                # write /output/entry.png
```
