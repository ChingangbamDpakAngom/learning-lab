# DSA: Big-O + two pointers

**Status:** ✅ done · **Sessions:** [25 Sep](../../log/2026-09-25_w0-d1/notes.md) · **Code:** [`drill/neetcode/`](../../drill/neetcode/) (contains duplicate, valid anagram, valid palindrome)
**Cheat sheets:** [Big-O](../../log/2026-09-25_w0-d1/Big-O-Cheat-Sheet.jpg) · [Two pointers](../../log/2026-09-25_w0-d1/Two-Pointers-Cheat-Sheet.jpg) · **Interview Qs:** [day 1 set](../../log/2026-09-25_w0-d1/Interview-Questions.md) · [short answers](../INTERVIEW-QA.md#big-o)

## Must know
**Big-O**
- How work grows as input n grows. Drop constants, keep the biggest term, name each input separately (O(a·b), not O(n²)).
- Reading code: sequential → add · nested → multiply · halving → log · hidden loops (`x in list`, slicing, `sorted`, `sum`) count.
- list `a[i]`, `append`, `pop()` O(1) · `insert(0, x)`, `pop(0)`, `x in list` O(n) · dict/set lookup O(1) average · `deque.popleft` O(1) · `heapq` push/pop O(log n).
- Space = extra memory only. `sorted(a)` O(n), `a.sort()` in place. Recursion depth d → O(d) stack.
- Key trade: spend O(n) memory (a set) to cut O(n²) time to O(n).
- Answer form: "O(__) time where n is __, because __; O(__) space for __."

**Two pointers**
- Two indices replace a nested loop: O(n²) → O(n), O(1) space.
- Templates: **opposite ends** (sorted pairs, palindrome, container) · **read/write** (in-place remove/move) · **two sequences** (merge, subsequence).
- Works because on sorted data every move rules out one element for good.
- Problems: Valid Palindrome · Two Sum II · Container With Most Water (move the shorter line) · 3Sum (sort + anchor + Two Sum II, skip duplicates).
- Pitfalls: `l < r` not `<=`, sort first, every branch must move a pointer.

## Mistakes I made
- Forgot **space** complexity every time.
- Said O(log n) for `a[len(a)//2]`: one index is O(1); binary search is log n only because it *repeats*.
- Merged two inputs into one n (two loops over a and b = O(a·b)).

## Gaps
- [ ] NeetCode backlog: Two Sum, Group Anagrams (Mon/Wed drill).
- [ ] Fast/slow pointers for linked lists (W4).
