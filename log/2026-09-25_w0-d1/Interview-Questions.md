# Day 1 Interview Questions · Big-O · Two pointers · Descriptive stats · Docker · Redis

How to use: read the question, **say your answer out loud** (as if to an interviewer), then click the callout to open the model answer. Mark ✅ / ½ / ❌ in the score table at the bottom. Redo the ❌ ones tomorrow.

Levels: 🟢 screening call · 🟡 technical round · 🔴 follow-up / senior-ish probe

---

## 1 · Big-O

> [!question]- Q1 🟢 What does Big-O tell you, and why do we drop constants?
> How the work (time or memory) **grows** as the input size n grows, usually in the worst case. Constants depend on the machine and language. They don't change how the cost *scales*, so O(2n) and O(n) are both "linear".

> [!question]- Q2 🟢 What's the time and space complexity?
> ```python
> def has_dup(a):
>     seen = set()
>     for x in a:
>         if x in seen: return True
>         seen.add(x)
>     return False
> ```
> **O(n) time**: one pass, and set lookup/add are O(1) on average. **O(n) space**: the set can hold every element.
> Say both. On Day 1 you forgot space every time.

> [!question]- Q3 🟡 Complexity of this?
> ```python
> for i in range(n):
>     for j in range(i, n):
>         work()
> ```
> **O(n²)**. It runs n + (n−1) + … + 1 = n(n+1)/2 times. After dropping the ½ and the lower-order term, that's n².

> [!question]- Q4 🟢 Complexity of this?
> ```python
> i = n
> while i > 1:
>     i //= 2
> ```
> **O(log n)**. Each step halves i, so it takes about log₂ n steps.

> [!question]- Q5 🟡 A function loops over list `a`, and inside that loop it loops over list `b`. Is that O(n²)?
> It's **O(a·b)**. They are two separate inputs, so give each its own letter. It's only O(n²) if both lists are the same size. (This was one of your Day 1 mistakes.)

> [!question]- Q6 🟡 Spot the hidden cost:
> ```python
> for x in a:
>     if x in b_list: count += 1
> ```
> `x in list` is itself an O(m) scan, so the total is **O(n·m)**. Fix: `b = set(b_list)` once (O(m)), then each lookup is O(1), giving **O(n + m) time and O(m) space**. You trade memory for time.

> [!question]- Q7 🟡 Why is `list.append` O(1) if the list sometimes has to resize?
> **Amortised O(1).** When the list is full, Python allocates a larger block and copies everything (O(n)). It grows by a proportion each time, so those copies are rare. Averaged over many appends, each one costs O(1).

> [!question]- Q8 🟡 Name three common Python operations that are O(n) but look cheap.
> Any three of these: `x in list`, `list.pop(0)`, `list.insert(0, x)`, slicing `a[i:j]`, `sum(a)`/`max(a)`, `s + t` string concatenation, `sorted(a)` (O(n log n)). Fix for queue-style pops: `collections.deque.popleft()`, which is O(1).

> [!question]- Q9 🔴 Dict lookup is O(1). Is it always?
> **Average** O(1) thanks to hashing. The worst case is **O(n)** when many keys collide into the same bucket. In practice Python's hashing makes that rare, but mention it: it shows you know "O(1)" is an average.

> [!question]- Q10 🟡 "Your solution is O(n²). Can you do better?" How do you think about it?
> Ask which work is repeated. The usual moves are:
> 1. **Hash set/map** to replace an inner search → O(n).
> 2. **Sort first**, then use two pointers or binary search → O(n log n).
> 3. **Two pointers / sliding window** on sorted or contiguous data → O(n).
>
> State the trade-off each time, e.g. "O(n) time, but O(n) extra space".

> [!question]- Q11 🟢 What's the space complexity of `s[::-1]` and of recursion depth d?
> `s[::-1]` builds a copy, so **O(n)**. Recursion keeps d frames on the call stack, so **O(d)**. For example, a recursive function on a balanced tree uses O(log n) stack space, and on a linked list O(n).

---

## 2 · Two pointers

> [!question]- Q12 🟢 When do you reach for two pointers?
> - **Sorted** array plus a pair or triplet with a target sum.
> - Palindrome or "compare both ends".
> - **In-place** removal or moving elements with O(1) space.
> - **Merging** two sorted sequences.
>
> The big signal is "sorted" + "pair", or "in place".

> [!question]- Q13 🟡 Why does opposite-ends Two Sum on a sorted array never miss the answer?
> If `a[L] + a[R]` is **too big**, then a[R] plus anything to its right of L is also too big, so a[R] can't be in any answer. Drop it (`R -= 1`). If the sum is **too small**, a[L] can't be in any answer, so drop it (`L += 1`). Each step safely removes one element, so the loop takes **O(n)** steps and never skips a valid pair.

> [!question]- Q14 🟡 Two Sum on an **unsorted** array that must return the original indices: two pointers or hash map?
> **Hash map**, O(n) time and O(n) space. Sorting costs O(n log n) *and* loses the original indices. Two pointers wins only when the input is already sorted, as in Two Sum II: O(1) space.

> [!question]- Q15 🟡 Code it: Valid Palindrome (ignore case and non-alphanumerics). State the complexity.
> ```python
> def is_pal(s):
>     l, r = 0, len(s) - 1
>     while l < r:
>         if not s[l].isalnum(): l += 1
>         elif not s[r].isalnum(): r -= 1
>         elif s[l].lower() != s[r].lower(): return False
>         else: l += 1; r -= 1
>     return True
> ```
> **O(n) time, O(1) space.** The cleaned-copy version `s == s[::-1]` is O(n) space. Mention it as the simple first answer, then improve.

> [!question]- Q16 🟡 Container With Most Water: why move the **shorter** line?
> Area = width × min(height). Moving either pointer shrinks the width. If you move the **taller** line, the min can't increase, because it's capped by the shorter line, so the area can only go down. Moving the shorter line is the only move that *might* find a bigger area.

> [!question]- Q17 🟡 3Sum: approach, complexity, and how do you avoid duplicate triplets?
> Sort. Then for each anchor i, run Two Sum II on `i+1..end` for target `-a[i]`. That's **O(n²) time** and O(1) extra space, not counting the output and the sort.
> Duplicates: skip an anchor equal to the previous one (`if i > 0 and a[i] == a[i-1]: continue`). After a hit, move `l` past equal values.

> [!question]- Q18 🟢 `while l < r` or `while l <= r`?
> For pairs, use `l < r`, because a pair needs two **different** elements. `l <= r` belongs to binary search, where one element can be the answer.

> [!question]- Q19 🟡 Code it: Move Zeroes in place, keeping the order of the non-zeros.
> ```python
> def move_zeroes(a):
>     w = 0
>     for r in range(len(a)):
>         if a[r] != 0:
>             a[w], a[r] = a[r], a[w]
>             w += 1
> ```
> This is the read/write pattern. `w` is where the next non-zero goes. **O(n) time, O(1) space.**

> [!question]- Q20 🟡 Merge two sorted lists of sizes n and m. Complexity?
> One pointer per list. Take the smaller value each time and append the leftovers at the end. **O(n + m) time**, O(n + m) for the output. Why not `sorted(a + b)`? It's O((n+m) log(n+m)), because it ignores that the lists are already sorted.

> [!question]- Q21 🔴 Name three bugs interviewers watch for in two-pointer code.
> - Forgetting to sort.
> - Using `<=` where it should be `<`.
> - A branch that moves no pointer, which means an infinite loop.
> - `r = len(a)` instead of `len(a) - 1`.
> - Not skipping duplicates in 3Sum.
> - Moving the wrong pointer in Container With Most Water.

---

## 3 · Descriptive statistics

> [!question]- Q22 🟢 Mean or median: which would you report for UK salaries, and why?
> **Median.** Salaries are **right-skewed**: a few very high earners pull the mean up, so it no longer describes a typical person. The median is robust to outliers. Whenever you see skew or outliers, report the median, ideally alongside the mean.

> [!question]- Q23 🟢 A distribution has mean > median. What does that tell you? Give a real example.
> It's **right-skewed** (a long tail of high values pulls the mean up). Examples: income, house prices, API latency, time on site.

> [!question]- Q24 🟡 Calculate by hand: variance and SD of `[1, 3, 5]`.
> Mean = 9/3 = 3. Deviations: −2, 0, 2. Squares: 4, 0, 4, which sum to **8**.
> - Population: 8/3 ≈ **2.67**, SD ≈ **1.63**
> - Sample (n−1): 8/2 = **4**, SD = **2**
>
> Say which one you're computing.

> [!question]- Q25 🟡 Why do we **square** the deviations instead of just adding them?
> Raw deviations always **sum to zero** (positives cancel negatives), so they tell you nothing. Squaring makes them all positive and **penalises big deviations more**. It's also smooth to differentiate, which is why MSE is the standard loss. Absolute deviations (MAE) also work and are more robust to outliers.

> [!question]- Q26 🟡 Why divide by **n − 1** for a sample?
> The sample mean is calculated from the same points, so it sits *closer* to them than the true population mean does. That makes the squared deviations too small, and dividing by n would **underestimate** the true variance. Dividing by n − 1 (Bessel's correction) fixes the bias. With large n, the difference barely matters.

> [!question]- Q27 🔴 `np.var(x)` and `pd.Series(x).var()` give different numbers. Why?
> Their defaults differ. NumPy uses **ddof=0** (divides by n, the population formula). pandas uses **ddof=1** (divides by n−1, the sample formula). Pass `ddof` explicitly so they match. This is a classic gotcha.

> [!question]- Q28 🟢 Why report SD rather than variance?
> SD is in the **same units** as the data (£, ms). Variance is in squared units (£²), which is hard to interpret.

> [!question]- Q29 🟡 How would you detect outliers? Which method for skewed data?
> - **IQR rule:** anything below Q1 − 1.5·IQR or above Q3 + 1.5·IQR (the box-plot whiskers). It's based on quartiles, so it's **robust**, which makes it good for **skewed** data.
> - **z-score:** |z| > 3. This assumes roughly **normal** data, and the outliers themselves inflate the mean and SD it's built from.
>
> Always look at the data (histogram or box plot) before removing anything. An outlier might be an error, or it might be the fraud case you're trying to catch.

> [!question]- Q30 🟢 What is a z-score, and what does z = 2.5 mean?
> z = (x − mean) / SD, the number of standard deviations from the mean. z = 2.5 means 2.5 SDs above average. For roughly normal data that's unusual: about 99% of values have |z| < 2.58.

> [!question]- Q31 🟢 What's the 68–95–99.7 rule? When doesn't it apply?
> For **normal** data, about 68% of values fall within ±1 SD, 95% within ±2 SD and 99.7% within ±3 SD. It **doesn't** hold for skewed or heavy-tailed data (latency, income), so check the shape first.

> [!question]- Q32 🟡 Why do teams monitor p95/p99 latency instead of the mean?
> Latency is right-skewed. The mean hides the slow tail, and a few very slow requests are exactly what users complain about. **p95 = 95% of requests are faster than this.** SLOs are usually written on p95/p99.

> [!question]- Q33 🟡 Why standardise features before training, and what's the common mistake?
> Features on big scales dominate distance-based models (KNN, K-means, SVM) and regularisation, and gradient descent converges faster on scaled data. Tree models don't need it.
> **Mistake: data leakage.** Fitting the scaler on the full dataset lets information from the test set leak into training. **Fit on train only**, then transform both train and test (or put the scaler inside a sklearn `Pipeline`).

> [!question]- Q34 🟡 Code it: given a pandas column `df["price"]`, flag outliers with the IQR rule.
> ```python
> q1, q3 = df["price"].quantile([0.25, 0.75])
> iqr = q3 - q1
> df["outlier"] = ~df["price"].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)
> ```
> Mention `df.describe()` as the first look at any new dataset.

---

## 4 · Docker

> [!question]- Q35 🟢 Image vs container?
> An **image** is a read-only template built from a Dockerfile, made of layers. A **container** is a running instance of an image, with its own writable layer on top. One image can run many containers. Analogy: a class and its objects.

> [!question]- Q36 🟢 Why use Docker for ML work?
> - **Reproducibility:** the same Python, libraries and system packages everywhere, which ends "works on my machine".
> - Easy **deployment** to any cloud or Kubernetes.
> - **Isolation** between projects.
> - Fast to start compared with VMs.

> [!question]- Q37 🟡 Container vs virtual machine?
> A VM runs a **full guest OS** on a hypervisor: heavy, slow to boot, strong isolation. Containers **share the host kernel**. Namespaces isolate them and cgroups limit their CPU and memory, which makes them light and quick to start (seconds), with weaker isolation.

> [!question]- Q38 🟡 Why copy `requirements.txt` and run `pip install` *before* copying the code?
> **Layer caching.** Docker rebuilds from the first changed layer onwards. Code changes often and dependencies rarely, so installing dependencies first keeps that slow layer cached. Rebuilds then take seconds instead of minutes.
> ```dockerfile
> COPY requirements.txt .
> RUN pip install --no-cache-dir -r requirements.txt
> COPY . .
> ```

> [!question]- Q39 🟡 The FastAPI app runs in a container, but `localhost:8000` doesn't respond. Two likely causes?
> 1. No port mapping. You need `-p 8000:8000` (HOST:CONTAINER).
> 2. The app listens on `127.0.0.1` *inside* the container. Bind it to **`0.0.0.0`** (`uvicorn app:app --host 0.0.0.0`).

> [!question]- Q40 🟡 The container restarted and the data is gone. Why, and how do you fix it?
> A container's writable layer is **temporary**. It's deleted along with the container. Use a **named volume** (`-v data:/var/lib/data`) for data that must persist. Use a bind mount for live code during development.

> [!question]- Q41 🟡 In Docker Compose, the API can't reach Redis at `localhost:6379`. Why?
> Inside a container, `localhost` is **that container**. Compose puts the services on a shared network where the **service name is the hostname**, so use `redis:6379`. Also, `depends_on` only controls start order. It doesn't wait until Redis is *ready*, so use a healthcheck or retry logic.

> [!question]- Q42 🔴 How do you keep an image small?
> - Use a slim base image (`python:3.12-slim`).
> - Run `pip install --no-cache-dir`.
> - Add a `.dockerignore` (exclude `.git`, data, venvs).
> - Use a **multi-stage build**: compile in one stage, copy only the result to the next.
> - Combine `RUN` steps.
> - Don't bake model weights or datasets into the image unless you have to.

> [!question]- Q43 🟢 `RUN` vs `CMD`?
> `RUN` executes at **build** time and creates a layer (for example, installing packages). `CMD` is the default command when the container **starts** (for example, launching uvicorn).

---

## 5 · Redis

> [!question]- Q44 🟢 What is Redis, and why is it so fast?
> An **in-memory** data-structure server (strings, hashes, lists, sets, sorted sets). It's fast because data lives in RAM, operations are simple, and a single thread runs commands one at a time with no lock contention.

> [!question]- Q45 🟢 Give four use cases.
> **Caching** (DB results, model predictions, embeddings) · **rate limiting** (`INCR` + `EXPIRE`) · **sessions** · **queues** (list + `BRPOP`) · **leaderboards** (sorted set) · pub/sub.

> [!question]- Q46 🟡 Walk me through the cache-aside pattern.
> **Read:** check Redis → hit: return it → miss: query the DB, `SET key value EX ttl`, return it.
> **Write:** update the DB, then **delete** the cache key so the next read refills it.
> Problems to mention:
> - **Stale data:** limited by the TTL.
> - **Cache stampede:** many misses hit the DB at once. Fix with a lock or TTL jitter.

> [!question]- Q47 🟡 What is a TTL for? What's the difference between TTL and eviction?
> A **TTL** is a lifetime *you* choose, so data expires and doesn't go stale forever. **Eviction** is what Redis does when **memory is full**, according to `maxmemory-policy`. For a cache, `allkeys-lru` removes the least recently used keys.

> [!question]- Q48 🔴 Two requests both do `GET count` then `SET count+1`. What goes wrong, and what's the fix?
> **Race condition / lost update.** Both read 5 and both write 6, so one increment is lost. Fix: `INCR count`. It's a single command, and Redis runs commands one at a time, so it's **atomic**. For multi-step logic, use `MULTI/EXEC` or a Lua script.

> [!question]- Q49 🟡 If Redis restarts, is the data lost?
> It depends on persistence:
> - **RDB:** periodic snapshots. Fast restart, but you can lose minutes of writes.
> - **AOF:** logs every write. With the usual `everysec` setting you lose about 1 s.
> - **None:** everything is lost, which is fine for a pure cache.
>
> You can combine RDB and AOF.

> [!question]- Q50 🟡 Why not store everything in Redis instead of Postgres?
> RAM is expensive and limited. Redis has weaker durability guarantees, and it has no SQL, joins, or rich queries. Redis sits **beside** the main database as a fast layer. It doesn't replace it.

---

## 6 · Scenario questions (put the day together)

> [!question]- Q51 🔴 "Our model API has p95 latency of 900 ms and the same inputs repeat often. What would you do?"
> 1. **Measure first:** is the time spent in preprocessing, the model, or I/O? Look at p50 vs p95.
> 2. **Cache** predictions in Redis, keyed by a hash of the normalised input, with a TTL. Invalidate the cache when the model version changes by putting the version in the key.
> 3. Track the **hit rate** and p95 before and after.
> 4. Run it with Docker Compose (api + redis). The API connects to `redis:6379`.
> Mention the trade-offs: stale predictions and extra memory.

> [!question]- Q52 🟡 "You get a new dataset. What do you do in the first 10 minutes?"
> - `df.shape`, `df.info()` (types, nulls), `df.describe()` (mean vs median to spot skew, min/max to spot impossible values).
> - A histogram or box plot of the key columns.
> - Check outliers with IQR.
> - Check duplicates.
> - Look at the target's class balance.
>
> Then decide how to clean the data. Never drop outliers blindly.

---

## Score (fill in: ✅ / ½ / ❌)

| Section | Qs | Score | Redo |
|---|---|---|---|
| Big-O | 1–11 | /11 | |
| Two pointers | 12–21 | /10 | |
| Descriptive stats | 22–34 | /13 | |
| Docker | 35–43 | /9 | |
| Redis | 44–50 | /7 | |
| Scenarios | 51–52 | /2 | |
