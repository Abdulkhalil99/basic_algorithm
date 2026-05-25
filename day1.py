"""
╔══════════════════════════════════════════════════════════════════╗
║           DSA FROM SCRATCH  —  Day 01: Big O Notation           ║
║                                                                  ║
║  The single most important concept in all of computer science.   ║
║  Before you write a single algorithm, you need to speak this     ║
║  language — because it tells you whether your code will run in   ║
║  1 second or 3 years.                                            ║
╚══════════════════════════════════════════════════════════════════╝

  WHAT IS BIG O?
  ──────────────
  Big O answers one question:

      "As my input grows, how does my code slow down?"

  It does NOT measure seconds. It measures GROWTH RATE.
  Two computers can run the same code — the faster machine
  gives different seconds but the SAME Big O.

  We always ask: what happens in the WORST CASE?
  We always DROP constants and smaller terms.

  THE COMPLETE COMPLEXITY LADDER (best → worst):
  ───────────────────────────────────────────────
  O(1)       → Constant    — instant, always
  O(log n)   → Log         — halves the problem each step
  O(n)       → Linear      — visits each element once
  O(n log n) → Log-linear  — best possible for sorting
  O(n²)      → Quadratic   — nested loops, gets bad fast
  O(2ⁿ)      → Exponential — explodes, avoid at all costs

  VISUAL GROWTH (operations for different input sizes):
  ──────────────────────────────────────────────────────
  Complexity  │  n=10    │  n=100      │  n=1,000
  ────────────┼──────────┼─────────────┼──────────────
  O(1)        │  1       │  1          │  1
  O(log n)    │  3       │  7          │  10
  O(n)        │  10      │  100        │  1,000
  O(n log n)  │  33      │  664        │  9,966
  O(n²)       │  100     │  10,000     │  1,000,000
  O(2ⁿ)       │  1,024   │  1.3×10³⁰  │  astronomical
"""

import time


# ══════════════════════════════════════════════════════════════════
#  1.  O(1) — CONSTANT TIME
# ══════════════════════════════════════════════════════════════════
#
#  No matter how large the input, you always do the SAME number
#  of operations. Size is irrelevant.
#
#  Real-world analogy:
#  Looking up a word if you already know the page number.
#  Doesn't matter if the dictionary has 100 or 100,000 pages.
#
#  Common examples: array index access, hash table lookup,
#                   push/pop from a stack, math operations.

def get_first_element(items):
    return items[0]          # always 1 operation

def get_last_element(items):
    return items[-1]         # always 1 operation, even for 1M items

def is_even(n):
    return n % 2 == 0        # always 1 operation

# Proof: time doesn't change as n grows
small = list(range(10))
large = list(range(10_000_000))

t1 = time.perf_counter(); get_first_element(small); t2 = time.perf_counter()
t3 = time.perf_counter(); get_first_element(large); t4 = time.perf_counter()

print("─" * 55)
print("O(1) — Constant Time")
print(f"  small list (10 items):       {(t2-t1)*1e6:.3f} μs")
print(f"  large list (10M items):      {(t4-t3)*1e6:.3f} μs")
print("  ↳ barely any difference — that's O(1)!")


# ══════════════════════════════════════════════════════════════════
#  2.  O(log n) — LOGARITHMIC TIME
# ══════════════════════════════════════════════════════════════════
#
#  Each step CUTS the remaining problem in half.
#  This is incredibly powerful — 1 billion items needs only 30 steps.
#
#  Real-world analogy:
#  Finding a name in a phone book. You open to the middle,
#  decide "too early" or "too late", discard half, repeat.
#
#  THE KEY INSIGHT: log₂(1,000,000,000) ≈ 30
#  One billion items → 30 comparisons. Mind-blowing.
#
#  Common examples: binary search, balanced BST operations,
#                   finding a number by guessing + feedback.

def binary_search(sorted_items, target):
    """
    Requires a SORTED list. Cuts search space in half each step.
    Returns the index of target, or -1 if not found.
    """
    left  = 0
    right = len(sorted_items) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2      # look at the middle

        if sorted_items[mid] == target:
            return mid, steps           # found it!
        elif sorted_items[mid] < target:
            left = mid + 1              # discard left half
        else:
            right = mid - 1            # discard right half

    return -1, steps                    # not found

# Prove the log growth: 10x more data, but barely more steps
data_10      = list(range(10))
data_100     = list(range(100))
data_1000    = list(range(1000))
data_million = list(range(1_000_000))

_, s1 = binary_search(data_10,      9)
_, s2 = binary_search(data_100,     99)
_, s3 = binary_search(data_1000,    999)
_, s4 = binary_search(data_million, 999_999)

print("\n" + "─" * 55)
print("O(log n) — Binary Search (searching for last element)")
print(f"  n=10:          {s1} step(s)")
print(f"  n=100:         {s2} step(s)")
print(f"  n=1,000:       {s3} step(s)")
print(f"  n=1,000,000:   {s4} step(s)")
print("  ↳ 100,000x more data, only a few extra steps!")


# ══════════════════════════════════════════════════════════════════
#  3.  O(n) — LINEAR TIME
# ══════════════════════════════════════════════════════════════════
#
#  You touch every element exactly once. Double the input,
#  double the work. Simple, predictable, often unavoidable.
#
#  Real-world analogy:
#  Reading every page of a book to count how many times
#  a word appears. No shortcut — you must check everything.
#
#  Common examples: find max/min, linear search, sum all items,
#                   copy an array, print all elements.

def linear_search(items, target):
    """No shortcut — check each element one by one."""
    for i, item in enumerate(items):    # n steps worst case
        if item == target:
            return i
    return -1

def find_max(items):
    """Must check every item — there's no way to skip any."""
    current_max = items[0]
    for item in items[1:]:              # n-1 steps
        if item > current_max:
            current_max = item
    return current_max

def count_occurrences(items, target):
    count = 0
    for item in items:                  # n steps, always
        if item == target:
            count += 1
    return count

sample = [3, 7, 1, 9, 4, 6, 2, 8, 5, 0]
print("\n" + "─" * 55)
print("O(n) — Linear Time")
print(f"  linear_search([...], 8) → index {linear_search(sample, 8)}")
print(f"  find_max([...])         → {find_max(sample)}")
print(f"  count_occurrences([...], 4) → {count_occurrences(sample, 4)}")
print("  ↳ n items = n steps, always proportional")


# ══════════════════════════════════════════════════════════════════
#  4.  O(n log n) — LOG-LINEAR TIME
# ══════════════════════════════════════════════════════════════════
#
#  The gold standard for sorting. You can NOT sort a general list
#  faster than O(n log n) — it's mathematically proven.
#
#  Real-world analogy:
#  Sorting a hand of cards by repeatedly splitting the deck in
#  half, sorting each half, then merging them back together.
#
#  MERGE SORT — Split → Sort → Merge
#
#  How it works:
#  [5, 2, 8, 1, 9, 3]
#     ↓ split in half
#  [5, 2, 8]   [1, 9, 3]
#     ↓ split again...
#  [5] [2,8]   [1] [9,3]
#     ↓ merge sorted halves
#  [2,5,8]   [1,3,9]
#     ↓ merge final
#  [1, 2, 3, 5, 8, 9]  ✓

def merge_sort(items):
    if len(items) <= 1:
        return items

    mid   = len(items) // 2
    left  = merge_sort(items[:mid])     # log n levels of recursion
    right = merge_sort(items[mid:])

    return _merge(left, right)

def _merge(left, right):
    """Merge two already-sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsorted = [5, 2, 8, 1, 9, 3, 7, 4, 6, 0]
print("\n" + "─" * 55)
print("O(n log n) — Merge Sort")
print(f"  input:  {unsorted}")
print(f"  sorted: {merge_sort(unsorted)}")
print("  ↳ Python's built-in sort() also uses O(n log n)")


# ══════════════════════════════════════════════════════════════════
#  5.  O(n²) — QUADRATIC TIME
# ══════════════════════════════════════════════════════════════════
#
#  A loop inside a loop. For every element, you loop through
#  ALL elements. This gets painful fast.
#
#  n=100    →       10,000 operations
#  n=1,000  →    1,000,000 operations
#  n=10,000 →  100,000,000 operations  (feels slow!)
#
#  Real-world analogy:
#  Comparing every person in a room to every other person
#  for a handshake. 10 people = 90 handshakes.
#  100 people = 9,900 handshakes.
#
#  BUBBLE SORT — the classic O(n²) example.
#  Each pass bubbles the largest unsorted item to its place.

def bubble_sort(items):
    """Sort by repeatedly swapping adjacent out-of-order pairs."""
    arr   = items.copy()
    n     = len(arr)
    steps = 0

    for i in range(n):                  # outer loop: n passes
        for j in range(n - i - 1):     # inner loop: n comparisons each
            steps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap

    print(f"  bubble_sort took {steps} comparisons for {n} items")
    return arr

def has_duplicate_naive(items):
    """O(n²) — check every pair."""
    for i in range(len(items)):
        for j in range(i + 1, len(items)):  # nested loop!
            if items[i] == items[j]:
                return True
    return False

def has_duplicate_fast(items):
    """O(n) — use a set instead. Same result, way faster."""
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

data = [64, 34, 25, 12, 22, 11, 90]
print("\n" + "─" * 55)
print("O(n²) — Bubble Sort")
print(f"  input:  {data}")
print(f"  sorted: {bubble_sort(data)}")

no_dups = list(range(1000))
print(f"\n  has_duplicate_naive (O(n²)): {has_duplicate_naive(no_dups)}")
print(f"  has_duplicate_fast  (O(n)):  {has_duplicate_fast(no_dups)}")
print("  ↳ same answer, but the set version is ~1000x faster!")


# ══════════════════════════════════════════════════════════════════
#  6.  O(2ⁿ) — EXPONENTIAL TIME
# ══════════════════════════════════════════════════════════════════
#
#  Every time n increases by 1, the work DOUBLES.
#  This is the danger zone. Only acceptable for tiny inputs.
#
#  fib(10)  →       177 calls
#  fib(20)  →    21,891 calls
#  fib(30)  → 2,692,537 calls
#  fib(50)  → would take longer than your lifetime
#
#  Real-world analogy:
#  A chain letter — you send to 2 friends, they each send to
#  2 friends, etc. Level 30 = over a billion people.

call_count = 0

def fib_exponential(n):
    """Naive recursion — calculates the SAME subproblems over and over."""
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fib_exponential(n - 1) + fib_exponential(n - 2)

def fib_linear(n):
    """O(n) — store results, never recalculate. This is memoization."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print("\n" + "─" * 55)
print("O(2ⁿ) vs O(n) — Fibonacci Comparison")
for n in [10, 20, 30]:
    call_count = 0
    result = fib_exponential(n)
    print(f"  fib_exponential({n:2d}) = {result:8d}  →  {call_count:>9,} recursive calls")

print()
for n in [10, 20, 30, 1000]:
    print(f"  fib_linear({n:4d})        = {fib_linear(n)}")
print("  ↳ O(n) handles n=1000 instantly. O(2ⁿ) would take forever.")


# ══════════════════════════════════════════════════════════════════
#  THE 3 RULES OF BIG O  (how to simplify)
# ══════════════════════════════════════════════════════════════════

print("\n" + "═" * 55)
print("THE 3 RULES")
print("═" * 55)

print("""
  RULE 1: Drop the constants
  ──────────────────────────
  O(2n)   →  O(n)     Two separate loops? Still linear.
  O(n/2)  →  O(n)     Half the elements? Still linear.
  O(100)  →  O(1)     100 fixed steps? Still constant.

  RULE 2: Drop the smaller terms
  ───────────────────────────────
  O(n² + n)    →  O(n²)    n² dominates completely
  O(n + log n) →  O(n)     n dominates log n
  O(2ⁿ + n¹⁰⁰) → O(2ⁿ)   exponential dominates all

  RULE 3: Different inputs = different variables
  ───────────────────────────────────────────────
  def process(list_a, list_b):
      for x in list_a:    ← depends on len(list_a)
          pass
      for y in list_b:    ← depends on len(list_b)
          pass

  This is O(a + b), NOT O(n).
  If it were nested loops: O(a × b), NOT O(n²).
""")


# ══════════════════════════════════════════════════════════════════
#  REAL-WORLD IMPACT — same problem, different complexities
# ══════════════════════════════════════════════════════════════════

print("═" * 55)
print("REAL-WORLD IMPACT")
print("  Assume 1 billion operations per second (modern CPU)")
print("═" * 55)

import math

def ops_to_time(ops):
    if ops > 1e18:
        return "longer than universe age"
    secs = ops / 1e9
    if secs < 0.001:   return f"{secs*1e6:.1f} μs"
    if secs < 1:       return f"{secs*1000:.1f} ms"
    if secs < 60:      return f"{secs:.1f} s"
    if secs < 3600:    return f"{secs/60:.1f} min"
    if secs < 86400:   return f"{secs/3600:.1f} hrs"
    return f"{secs/86400:.0f} days"

complexities_named = [
    ("O(1)",       lambda n: 1),
    ("O(log n)",   lambda n: math.log2(n)),
    ("O(n)",       lambda n: n),
    ("O(n log n)", lambda n: n * math.log2(n)),
    ("O(n²)",      lambda n: n ** 2),
    ("O(2ⁿ)",      lambda n: 2 ** n),
]

sizes = [100, 10_000, 1_000_000]
header = f"  {'Complexity':<14}" + "".join(f"{'n='+str(n):>20}" for n in sizes)
print(header)
print("  " + "─" * (14 + 20 * len(sizes)))
for name, fn in complexities_named:
    row = f"  {name:<14}"
    for n in sizes:
        try:
            ops = fn(n)
            row += f"{ops_to_time(ops):>20}"
        except OverflowError:
            row += f"{'∞':>20}"
    print(row)


# ══════════════════════════════════════════════════════════════════
#  PRACTICE EXERCISES
# ══════════════════════════════════════════════════════════════════

print("\n" + "═" * 55)
print("EXERCISES — figure out the Big O of each function")
print("═" * 55)
print("""
  Exercise 1:
  ────────────
  def mystery_a(n):
      result = 0
      while n > 1:
          n = n // 2       # what does this do each step?
          result += 1
      return result
  Answer: O(_____)

  Exercise 2:
  ────────────
  def mystery_b(items):
      for i in range(len(items)):
          for j in range(i, len(items)):
              print(items[i], items[j])
  Answer: O(_____)

  Exercise 3:
  ────────────
  def mystery_c(items):
      seen = {}
      for item in items:
          seen[item] = seen.get(item, 0) + 1
      return max(seen, key=seen.get)
  Answer: O(_____)

  Exercise 4 (trick question):
  ─────────────────────────────
  def mystery_d(n):
      for i in range(1000):
          print(i)
  Answer: O(_____)

  ──────────────────────────────
  ANSWERS (scroll down after thinking!)
  .
  .
  .
  .
  .
  .
  1) O(log n)  — halves n each step
  2) O(n²)     — nested loops, ~n²/2 pairs → drop constant → O(n²)
  3) O(n)      — one loop, dict ops are O(1)
  4) O(1)      — 1000 fixed iterations, doesn't depend on n at all!
""")

print("═" * 55)
print("Day 01 complete. Next: Day 02 — Arrays")
print("═" * 55)