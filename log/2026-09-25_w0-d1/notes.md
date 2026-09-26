# Fri 25 Sep 2026 · Week 0, Day 1

Order: DSA → Engineering → Theory (job ads) → Career

## DSA · Big-O ✅
- Big-O = how work grows as input n grows. Drop constants, keep the biggest term, name each input separately (O(a·b), not O(n²)).
- Reading code: sequential → add · nested → multiply · halving → log · hidden loops (`x in list`, slicing, `sorted`, `sum`) count.
- List: `a[i]`, `append`, `pop()` O(1) · `insert(0, x)`, `pop(0)`, `x in list` O(n). Dict/set lookups O(1) average (hashing). `deque.popleft` O(1). `heapq` push/pop O(log n).
- Space: extra memory only. `sorted(a)` O(n), `a.sort()` in place. Recursion depth d → O(d) stack.
- Key trade: spend O(n) memory (a set) to cut O(n²) time to O(n).
- Interview answer form: "O(__) time where n is __, because __; O(__) space for __."
- Generated: [Big-O-Cheat-Sheet.jpg](Big-O-Cheat-Sheet.jpg) (source: `Big-O-Cheat-Sheet.source.html`)

### Quiz: 5 / 7
| # | Code | My answer | Correct (time / space) |
|---|---|---|---|
| 1 | `a[len(a)//2]` | O(log n) ❌ | O(1) / O(1): one index, no loop. Binary search is log n only because it *repeats* the middle step |
| 2 | two separate loops | O(n) ✅ | O(n) / O(1) |
| 3 | loop a × loop b | O(n²) ½ | O(a·b) / O(1): two inputs, two letters |
| 4 | `i *= 2` until n | O(log n) ✅ | O(log n) / O(1) |
| 5 | sort then scan | O(n log n) ✅ | O(n log n) / O(n) (`sorted` copies) |
| 6 | count with dict | O(n) ✅ | O(n) / O(n) (O(k) distinct) |
| 7 | `insert(0, x)` in loop | O(n²) ✅ | O(n²) / O(n) |

**Mistakes to remember:** forgot space every time; confused "middle" with binary search; merged two inputs into one n.

## DSA · Two pointers (ahead of plan: week 2 topic) ✅
- Two indices replace a nested loop: O(n²) → O(n), O(1) extra space.
- Three templates: **opposite ends** (sorted pairs, palindrome, container) · **read/write** (in-place remove/move) · **two sequences** (merge, subsequence). Fast/slow for linked lists comes in week 4.
- Why it works: on sorted data every move rules out one element for good (sum too big → drop the right; too small → drop the left).
- Problems: Valid Palindrome (skip non-alphanumerics) · Two Sum II (template A, 1-indexed) · Container With Most Water (move the shorter line) · 3Sum (sort + anchor + Two Sum II, skip duplicates, O(n²)).
- Pitfalls: `l < r` not `<=`, sort first, skip 3Sum duplicates, every branch must move a pointer.
- Generated: [Two-Pointers-Cheat-Sheet.jpg](Two-Pointers-Cheat-Sheet.jpg)

## ML core · Descriptive statistics (taught, practical pending)
- Centre: mean (pulled by outliers) vs **median** (robust) vs mode (categories). Skewed data → report the median.
- Spread: variance = average squared deviation; **SD** = √variance, back in original units. Sample → divide by n−1 (`np.var` ddof=0 vs pandas ddof=1!). Range (fragile), **IQR** = Q3 − Q1 (robust).
- Outliers: beyond Q1 − 1.5·IQR or Q3 + 1.5·IQR (box plot); |z| > 3 for roughly normal data.
- Shape: histogram first. Right skew → mean > median (income, latency). Mean is pulled toward the tail.
- z = (x − mean)/SD → StandardScaler. Production: latency p50/p95/p99, CV results as mean ± SD, drift = comparing distributions.
- Generated: [Descriptive-Statistics-Cheat-Sheet.jpg](Descriptive-Statistics-Cheat-Sheet.jpg)

## Engineering · Docker + Redis ⬜
**Docker:** Dockerfile (recipe) → image (read-only layers) → container (running instance + writable layer); registry shares images.
- Copy `requirements.txt` before code so the `pip install` layer stays cached. `--host 0.0.0.0` inside containers.
- Container vs VM: containers share the host kernel (namespaces isolate, cgroups limit); VMs run a full guest OS.
- `-p HOST:CONTAINER` maps ports. Containers are temporary → named volumes for data, bind mounts for dev code.
- Compose: service name = hostname (`redis:6379`, not localhost). `depends_on` = start order only, not "ready".

**Redis:** in-memory data-structure server; single thread runs commands one at a time → every command is atomic.
- Types: string (cache, `INCR` counter) · hash (object) · list (queue, `BRPOP`) · set (membership) · sorted set (leaderboard).
- TTL = you choose the lifetime; eviction (`maxmemory-policy`, e.g. `allkeys-lru`) = what happens when memory is full.
- Persistence: RDB snapshots (fast load, lose minutes) vs AOF log (lose ~1 s).
- Cache-aside: read cache → miss → DB → set with TTL; on write, delete the key. Problems: stale data, stampede (lock / TTL jitter).
- Race: GET→SET loses updates; `INCR`, `MULTI/EXEC` or Lua make it atomic. Fixed-window limiter = `INCR` + `EXPIRE` (burst at the window edge).
- Redis sits beside the main database, not in place of it.

- [ ] `docker run -d --name r -p 6379:6379 redis:7`, then `docker exec -it r redis-cli`
- [ ] Strings (`SET/GET/INCR`), hashes (`HSET/HGETALL`), TTL (`SET k v EX 10`, `TTL k`)
- [ ] Answer: container vs VM · Redis vs app memory · data on restart (RDB/AOF) · what TTL is for

## Theory · Job-ad tally ⬜
- [ ] 10 UK ML/AI Engineer ads → tick Python, SQL, PyTorch, Docker, Cloud, K8s, LLM/RAG, MLOps, Stats · note top 5

## Career · GitHub cleanup ⬜
- [ ] Normal-case name, bio, location, LinkedIn link; delete the two unused forks

## Interview practice
- [Interview-Questions.md](Interview-Questions.md): 52 questions across all of today's topics, with collapsible answers and a score table

## Open questions
-
