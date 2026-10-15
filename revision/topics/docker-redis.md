# Docker + Redis

**Status:** 🟡 theory only · **Sessions:** [25 Sep](../../log/2026-09-25_w0-d1/notes.md) · **Interview Qs:** [Docker Qs](../../log/2026-09-27_w0-d3/docker-questions.md) · [day 1 set §4–5](../../log/2026-09-25_w0-d1/Interview-Questions.md) · short answers: [Docker](../INTERVIEW-QA.md#docker), [Redis](../INTERVIEW-QA.md#redis)

## Must know
**Docker**
- Dockerfile (recipe) → image (read-only layers) → container (running instance + writable layer); a registry shares images.
- Copy `requirements.txt` before the code so the `pip install` layer stays cached. `--host 0.0.0.0` inside containers.
- Container vs VM: containers share the host kernel (namespaces isolate, cgroups limit); VMs run a full guest OS.
- `-p HOST:CONTAINER` maps ports. Containers are temporary → named volumes for data, bind mounts for dev code.
- Compose: service name = hostname (`redis:6379`, not localhost). `depends_on` = start order only, not "ready".

**Redis**
- In-memory data-structure server; one thread runs commands one at a time → every command is atomic.
- Types: string (cache, `INCR`) · hash (object) · list (queue) · set (membership) · sorted set (leaderboard).
- TTL = lifetime you choose; eviction (`allkeys-lru`) = what happens when memory is full.
- Persistence: RDB snapshots (lose minutes) vs AOF log (lose ~1 s).
- Cache-aside: read cache → miss → DB → set with TTL; on write, delete the key. Risks: stale data, stampede.
- GET→SET loses updates; `INCR` / `MULTI/EXEC` / Lua are atomic. Redis sits beside the main DB, not instead of it.

## Mistakes I made
- None recorded yet.

## Gaps
- [ ] Hands-on: `docker run -d --name r -p 6379:6379 redis:7` → `redis-cli`: SET/GET/INCR, HSET, `SET k v EX 10` + `TTL k`.
- [ ] Docker deploy for real in W7 (lab 13).
