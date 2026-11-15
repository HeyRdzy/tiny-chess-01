[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/HeyRdzy/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/HeyRdzy/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess-01

A 4 KB Python chess engine for [make.fun's tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01): build the strongest chess engine in 4,096 bytes of Python.

`main.py` (2,618 bytes, LZMA-packed from the readable `main_src.py`) plays every game through the env. It is a 0x88 negamax + alpha-beta search with quiescence (SEE filter that skips losing captures), null-move pruning, a transposition table with bounds, killer moves, full piece-square tables plus a bishop-pair bonus, and an adaptive node budget (130k) that stops deepening when a depth costs too much, so no move comes near the 10 s limit.

Practice trials (6 games, first 6 house opponents): v10 scores 4.0/6 (Elo 1451) on trial-0 and 2.0/6 (Elo 1099) on trial-1, 6.0/12 combined (Elo 1279) — above the 1,154 practice floor.

## The size rule

- `main.py` is the whole engine: at most 4,096 bytes as committed, Python 3.13, standard library only. It reads, imports or execs no other file in the repository.
- Compression is allowed and counted. A `main.py` that unpacks and execs a compressed payload (`lzma`) is fine; the payload and the unpacker are both part of its 4,096 bytes.
- The rest of the tree (this README, LICENSE) is at most 8,192 bytes in all, and no file over 4,096.
- Search to a fixed depth or node count, never a clock: a final contender's trials are replayed and must play the same moves.
