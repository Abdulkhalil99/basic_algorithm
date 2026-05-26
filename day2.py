"""
╔══════════════════════════════════════════════════════════════════╗
║              DSA FROM SCRATCH  —  Day 02: Arrays                ║
║                                                                  ║
║  The most fundamental data structure in all of programming.      ║
║  Every other structure — stacks, queues, heaps — is often        ║
║  built on top of arrays. Understand this deeply.                 ║
╚══════════════════════════════════════════════════════════════════╝

  WHAT IS AN ARRAY?
  ─────────────────
  A collection of items stored in CONTIGUOUS (side-by-side)
  memory locations, each accessible by an INDEX.

  Memory layout (each box = 1 memory address):
  ┌─────┬─────┬─────┬─────┬─────┐
  │  10 │  20 │  30 │  40 │  50 │
  └─────┴─────┴─────┴─────┴─────┘
  addr: 1000  1001  1002  1003  1004
  index:  [0]   [1]   [2]   [3]   [4]

  WHY IS index ACCESS O(1)?
  ─────────────────────────
  address = start_address + (index × element_size)
  items[3] → 1000 + (3 × 1) = address 1003  → instant!
  No matter how big the array, it's always ONE calculation.

  TWO KINDS OF ARRAYS:
  ─────────────────────
  Static  → fixed size, set at creation (C, Java int[])
  Dynamic → grows automatically (Python list, Java ArrayList)
  Python lists are DYNAMIC arrays under the hood.

  BIG O CHEAT SHEET FOR ARRAYS:
  ───────────────────────────────
  Access by index    →  O(1)   ← best possible
  Search (unsorted)  →  O(n)   ← must check each
  Search (sorted)    →  O(log n) ← binary search
  Insert at end      →  O(1) amortized ← usually
  Insert at middle   →  O(n)   ← must shift elements
  Delete at end      →  O(1)
  Delete at middle   →  O(n)   ← must shift elements
"""


# ══════════════════════════════════════════════════════════════════
#  1.  ARRAY BASICS — creation, access, slicing
# ══════════════════════════════════════════════════════════════════

print("═" * 57)
print("1. ARRAY BASICS")
print("═" * 57)

# Creating arrays (Python lists)
empty   = []
numbers = [10, 20, 30, 40, 50]
mixed   = [1, "hello", 3.14, True]      # Python allows mixed types
zeros   = [0] * 5                        # [0, 0, 0, 0, 0]
squares = [x**2 for x in range(6)]      # list comprehension

print(f"numbers:    {numbers}")
print(f"zeros:      {zeros}")
print(f"squares:    {squares}")

# Index access — O(1)
print(f"\nIndex access O(1):")
print(f"  numbers[0]  = {numbers[0]}   (first)")
print(f"  numbers[4]  = {numbers[4]}  (last by index)")
print(f"  numbers[-1] = {numbers[-1]}  (last, pythonic)")
print(f"  numbers[-2] = {numbers[-2]}  (second to last)")

# Slicing — O(k) where k = slice length
print(f"\nSlicing O(k):")
print(f"  numbers[1:4]  = {numbers[1:4]}    (index 1 up to, not including 4)")
print(f"  numbers[:3]   = {numbers[:3]}  (first 3)")
print(f"  numbers[2:]   = {numbers[2:]}  (from index 2 to end)")
print(f"  numbers[::-1] = {numbers[::-1]}  (reversed)")


# ══════════════════════════════════════════════════════════════════
#  2.  HOW DYNAMIC ARRAYS GROW  (the secret behind Python lists)
# ══════════════════════════════════════════════════════════════════

print("\n" + "═" * 57)
print("2. HOW DYNAMIC ARRAYS GROW UNDER THE HOOD")
print("═" * 57)

print("""
  Problem: arrays live in contiguous memory.
  If you append and the next slot is taken — what happens?

  Answer: Python DOUBLES the capacity when it runs out.

  Step 1: Start with capacity 4
  ┌────┬────┬────┬────┐
  │ 10 │ 20 │ 30 │ 40 │  ← full!
  └────┴────┴────┴────┘

  Step 2: Append 50 — no room! Allocate new array (capacity 8),
          COPY all old elements, add new one.
  ┌────┬────┬────┬────┬────┬────┬────┬────┐
  │ 10 │ 20 │ 30 │ 40 │ 50 │    │    │    │
  └────┴────┴────┴────┴────┴────┴────┴────┘

  Why is append still O(1) "amortized"?
  ─────────────────────────────────────
  Resizing is O(n) but it happens RARELY (only when capacity
  doubles). Averaged across all appends, each one costs O(1).
  This is called AMORTIZED analysis.
""")

import sys

arr = []
prev_size = sys.getsizeof(arr)
print("  Watching Python list grow (size in bytes):")
print(f"  {'items':>6} │ {'bytes':>6} │ note")
print(f"  {'──────':>6}─┼─{'──────':>6}─┼────────────────")
for i in range(17):
    arr.append(i)
    size = sys.getsizeof(arr)
    note = " ← RESIZED (new memory allocated)" if size != prev_size else ""
    print(f"  {len(arr):>6} │ {size:>6} │{note}")
    prev_size = size


# ══════════════════════════════════════════════════════════════════
#  3.  CORE OPERATIONS WITH BIG O PROOF
# ══════════════════════════════════════════════════════════════════

print("\n" + "═" * 57)
print("3. CORE OPERATIONS — with Big O explained")
print("═" * 57)

# ── READ — O(1) ──────────────────────────────────────────────────
print("\n── READ  O(1) ──")
nums = [10, 20, 30, 40, 50]
print(f"  nums = {nums}")
print(f"  nums[2] = {nums[2]}   ← one calculation, instant")

# ── SEARCH — O(n) unsorted ───────────────────────────────────────
print("\n── SEARCH  O(n) unsorted ──")

def linear_search(arr, target):
    """Check every element until we find it or exhaust the array."""
    for i in range(len(arr)):       # worst case: all n elements
        if arr[i] == target:
            return i                # found at index i
    return -1                       # not found

data = [7, 2, 9, 4, 1, 8, 3, 6, 5]
print(f"  array:  {data}")
print(f"  search 8 → index {linear_search(data, 8)}   (checked up to 6 elements)")
print(f"  search 5 → index {linear_search(data, 5)}   (checked all 9 elements — worst case)")
print(f"  search 99 → index {linear_search(data, 99)}  (checked all 9, not found)")

# ── SEARCH — O(log n) sorted ─────────────────────────────────────
print("\n── SEARCH  O(log n) sorted — Binary Search ──")

def binary_search(arr, target):
    """
    REQUIRES sorted array.
    Each step eliminates HALF the remaining elements.

    Visual for searching 7 in [1,2,3,4,5,6,7,8,9]:
    Step 1: mid=4 (value 5) → 7 > 5 → go RIGHT
            [_ _ _ _ _ 6 7 8 9]
    Step 2: mid=7 (value 8) → 7 < 8 → go LEFT
            [_ _ _ _ _ 6 7 _ _]
    Step 3: mid=6 (value 7) → FOUND at index 6 ✓
    """
    left, right = 0, len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1          # discard left half
        else:
            right = mid - 1         # discard right half

    return -1, steps

sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
idx, steps = binary_search(sorted_data, 7)
print(f"  sorted: {sorted_data}")
print(f"  search 7 → index {idx} in {steps} steps  (linear would take up to 9)")

# Show the log n proof:
print(f"\n  Proof that binary search is O(log n):")
import math
for n in [10, 100, 1000, 1_000_000, 1_000_000]:
    arr2 = list(range(n))
    _, s = binary_search(arr2, n-1)    # worst case: search for last element
    theoretical = math.ceil(math.log2(n))
    print(f"    n={n:>12,} → {s:>2} steps  (log₂({n:,}) ≈ {theoretical})")

# ── INSERT ───────────────────────────────────────────────────────
print("\n── INSERT ──")

def insert_at_end(arr, value):
    """O(1) amortized — just add to the end."""
    arr.append(value)
    return arr

def insert_at_index(arr, index, value):
    """
    O(n) — must shift all elements AFTER index one spot right.

    Inserting 99 at index 2 in [10, 20, 30, 40, 50]:
    Step 1: shift 50 → index 5:  [10, 20, 30, 40, 50, 50]
    Step 2: shift 40 → index 4:  [10, 20, 30, 40, 40, 50]
    Step 3: shift 30 → index 3:  [10, 20, 30, 30, 40, 50]
    Step 4: place 99 at index 2: [10, 20, 99, 30, 40, 50] ✓
    """
    arr.insert(index, value)
    return arr

nums = [10, 20, 30, 40, 50]
print(f"  original:                 {nums}")
print(f"  insert_at_end(99):        {insert_at_end(nums[:], 99)}  O(1)")
print(f"  insert_at_index(2, 99):   {insert_at_index(nums[:], 2, 99)}  O(n) — shifted 3 elements")
print(f"  insert_at_index(0, 99):   {insert_at_index(nums[:], 0, 99)}  O(n) — shifted ALL 5 (worst case)")

# ── DELETE ───────────────────────────────────────────────────────
print("\n── DELETE ──")

def delete_at_end(arr):
    """O(1) — just remove the last element."""
    return arr.pop()

def delete_at_index(arr, index):
    """
    O(n) — must shift all elements AFTER index one spot LEFT.

    Deleting index 1 from [10, 20, 30, 40, 50]:
    Step 1: remove 20
    Step 2: shift 30 → index 1: [10, 30, 40, 50]
    Step 3: shift 40 → index 2: [10, 30, 40, 50]
    Step 4: shift 50 → index 3: [10, 30, 40, 50] ✓
    """
    return arr.pop(index)

nums = [10, 20, 30, 40, 50]
a = nums[:]; deleted = delete_at_end(a)
print(f"  delete_at_end():          removed {deleted}, left {a}  O(1)")
b = nums[:]; deleted = delete_at_index(b, 1)
print(f"  delete_at_index(1):       removed {deleted}, left {b}  O(n)")


# ══════════════════════════════════════════════════════════════════
#  4.  2D ARRAYS (MATRICES)
# ══════════════════════════════════════════════════════════════════

print("\n" + "═" * 57)
print("4. 2D ARRAYS — arrays of arrays")
print("═" * 57)

print("""
  A 2D array is a grid. Think of a chessboard,
  a spreadsheet, or a pixel image.

  matrix[row][col]
  ┌──────────────────────┐
  │  col→  0   1   2     │
  │  row 0: 1   2   3    │
  │  row 1: 4   5   6    │
  │  row 2: 7   8   9    │
  └──────────────────────┘
""")

# Create a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("  matrix:")
for row in matrix:
    print(f"    {row}")

print(f"\n  matrix[0][0] = {matrix[0][0]}  (top-left)")
print(f"  matrix[1][1] = {matrix[1][1]}  (center)")
print(f"  matrix[2][2] = {matrix[2][2]}  (bottom-right)")

# Traverse all elements — O(n×m)
print(f"\n  Traversing all elements O(rows × cols):")
total = 0
for row in matrix:
    for val in row:
        total += val
print(f"  Sum of all elements = {total}")

# Create matrix with list comprehension
def create_matrix(rows, cols, default=0):
    return [[default] * cols for _ in range(rows)]

m = create_matrix(3, 4, default=0)
print(f"\n  create_matrix(3, 4) = {m}")


# ══════════════════════════════════════════════════════════════════
#  5.  CLASSIC ARRAY PROBLEMS  (interview favorites)
# ══════════════════════════════════════════════════════════════════

print("\n" + "═" * 57)
print("5. CLASSIC ARRAY PROBLEMS")
print("═" * 57)

# ── Problem 1: Reverse an array ───────────────────────────────────
print("\n── Problem 1: Reverse an array  O(n) ──")
print("""
  Approach: two pointers — one at start, one at end.
  Swap them and move inward until they meet.

  [1, 2, 3, 4, 5]
   ↑           ↑   swap → [5, 2, 3, 4, 1]
      ↑     ↑       swap → [5, 4, 3, 2, 1]
         ↑           mid  → done!
""")

def reverse_array(arr):
    arr = arr.copy()
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left  += 1
        right -= 1
    return arr

print(f"  input:  [1, 2, 3, 4, 5]")
print(f"  output: {reverse_array([1, 2, 3, 4, 5])}")

# ── Problem 2: Find duplicates ────────────────────────────────────
print("\n── Problem 2: Find duplicates  O(n) with set ──")
print("""
  Naive approach: compare every pair → O(n²)  ✗
  Smart approach: use a set to track seen items → O(n)  ✓

  Walk through [1, 3, 4, 2, 2, 7, 3]:
  seen={} → add 1 → {1}
  seen={1} → add 3 → {1,3}
  seen={1,3} → add 4 → {1,3,4}
  seen={1,3,4} → add 2 → {1,2,3,4}
  seen={1,2,3,4} → 2 already in seen! → DUPLICATE ✓
""")

def find_duplicates(arr):
    seen = set()
    duplicates = []
    for item in arr:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

data = [1, 3, 4, 2, 2, 7, 3, 1]
print(f"  input:      {data}")
print(f"  duplicates: {find_duplicates(data)}")

# ── Problem 3: Two Sum ────────────────────────────────────────────
print("\n── Problem 3: Two Sum  O(n) ──")
print("""
  Given an array and a target, find TWO numbers that add to target.
  Return their indices.

  Naive: try every pair → O(n²)  ✗
  Smart: for each number x, check if (target - x) exists → O(n)  ✓

  Walk through [2, 7, 11, 15], target = 9:
  i=0: x=2, need 7. seen={}. Not found. Store {2: 0}
  i=1: x=7, need 2. seen={2:0}. FOUND! → return [0, 1] ✓
""")

def two_sum(arr, target):
    seen = {}                               # value → index
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]    # found the pair!
        seen[x] = i
    return []                               # no pair found

print(f"  two_sum([2, 7, 11, 15], target=9)  → {two_sum([2, 7, 11, 15], 9)}")
print(f"  two_sum([3, 2, 4, 1],   target=6)  → {two_sum([3, 2, 4, 1], 6)}")
print(f"  two_sum([1, 5, 3, 7],   target=12) → {two_sum([1, 5, 3, 7], 12)}")

# ── Problem 4: Max subarray sum (Kadane's Algorithm) ─────────────
print("\n── Problem 4: Maximum Subarray Sum  O(n) — Kadane's Algorithm ──")
print("""
  Given an array, find the contiguous subarray with the largest sum.
  This is one of the most famous array algorithms.

  Key insight: at each position, decide:
  "Is it better to EXTEND the current subarray, or START FRESH?"

  Walk through [-2, 1, -3, 4, -1, 2, 1, -5, 4]:
  pos: -2  →  current=-2,  best=-2
  pos:  1  →  extend: -2+1=-1  vs  start: 1  → pick 1
  pos: -3  →  extend: 1-3=-2   vs  start:-3  → pick -2
  pos:  4  →  extend: -2+4=2   vs  start: 4  → pick 4
  pos: -1  →  extend: 4-1=3    vs  start:-1  → pick 3  best=4
  pos:  2  →  extend: 3+2=5    vs  start: 2  → pick 5  best=5
  pos:  1  →  extend: 5+1=6    vs  start: 1  → pick 6  best=6 ✓
  ...
  Answer: 6  (subarray [4, -1, 2, 1])
""")

def max_subarray(arr):
    current_sum = arr[0]
    best_sum    = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]            # start fresh
            temp_start  = i
        else:
            current_sum += arr[i]           # extend

        if current_sum > best_sum:
            best_sum  = current_sum
            start     = temp_start
            end       = i

    return best_sum, arr[start:end+1]

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
best, sub = max_subarray(arr)
print(f"  input:           {arr}")
print(f"  max sum:         {best}")
print(f"  best subarray:   {sub}")


# ══════════════════════════════════════════════════════════════════
#  6.  PYTHON-SPECIFIC ARRAY TRICKS  (write cleaner code)
# ══════════════════════════════════════════════════════════════════

print("\n" + "═" * 57)
print("6. PYTHON ARRAY TRICKS  (write pro-level code)")
print("═" * 57)

nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(f"\n  nums = {nums}")
print(f"  len(nums)         = {len(nums)}")
print(f"  min(nums)         = {min(nums)}")
print(f"  max(nums)         = {max(nums)}")
print(f"  sum(nums)         = {sum(nums)}")
print(f"  sorted(nums)      = {sorted(nums)}          ← doesn't modify original")
print(f"  nums after        = {nums}       ← unchanged")

nums_copy = nums[:]
nums_copy.sort()
print(f"  .sort() in-place  = {nums_copy}     ← modifies the list")

print(f"\n  Enumerate (index + value together):")
for i, val in enumerate([10, 20, 30]):
    print(f"    i={i}, val={val}")

print(f"\n  Zip (combine two arrays):")
names  = ["Alice", "Bob", "Carol"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"    {name}: {score}")

print(f"\n  List comprehension patterns:")
print(f"  squares:  {[x**2 for x in range(1,6)]}")
print(f"  evens:    {[x for x in range(10) if x % 2 == 0]}")
print(f"  2D flat:  {[matrix[r][c] for r in range(3) for c in range(3)]}")


# ══════════════════════════════════════════════════════════════════
#  FULL BIG O SUMMARY
# ══════════════════════════════════════════════════════════════════

print("\n" + "═" * 57)
print("ARRAY BIG O — COMPLETE REFERENCE")
print("═" * 57)
print("""
  Operation              │ Time    │ Why
  ───────────────────────┼─────────┼──────────────────────────
  Read  arr[i]           │ O(1)    │ direct address calculation
  Write arr[i] = x       │ O(1)    │ direct address calculation
  Search (unsorted)      │ O(n)    │ must check every element
  Search (sorted)        │ O(log n)│ binary search halves space
  Insert at end          │ O(1)*   │ *amortized, rare O(n) resize
  Insert at middle/start │ O(n)    │ must shift elements right
  Delete at end          │ O(1)    │ just reduce length
  Delete at middle/start │ O(n)    │ must shift elements left
  Slice arr[i:j]         │ O(k)    │ k = number of elements copied
  Sort                   │ O(n log n) │ best possible comparison sort
  ───────────────────────┴─────────┴──────────────────────────
  Space complexity: O(n) — stores n elements
""")


# ══════════════════════════════════════════════════════════════════
#  EXERCISES
# ══════════════════════════════════════════════════════════════════

print("═" * 57)
print("EXERCISES — solve these before Day 03")
print("═" * 57)
print("""
  Exercise 1:
  ────────────
  Write a function rotate_right(arr, k) that rotates an array
  k positions to the right IN-PLACE.
  rotate_right([1,2,3,4,5], 2) → [4, 5, 1, 2, 3]
  What is the Big O of your solution?

  Exercise 2:
  ────────────
  Write a function remove_duplicates(arr) that removes
  duplicates from a SORTED array and returns the new length.
  Do it with O(1) extra space (no creating a new array).
  remove_duplicates([1,1,2,2,3,4,4,5]) → 5  (keeps [1,2,3,4,5])

  Exercise 3:
  ────────────
  Write a function merge_sorted(a, b) that merges two
  SORTED arrays into one sorted array.
  merge_sorted([1,3,5], [2,4,6]) → [1,2,3,4,5,6]
  What is the Big O?

  Exercise 4 (challenge):
  ────────────────────────
  Write a function find_missing(arr) that finds the one missing
  number in an array containing 1 to n with one number missing.
  find_missing([1,2,4,5,6]) → 3
  Hint: sum(1..n) = n*(n+1)//2
  What is the Big O, and can you do it in O(1) space?

  ──────────────────────────────
  ANSWERS (think first!)
  .
  .
  .
  .
  .
  .
  Ex 1: arr[:] = arr[-k:] + arr[:-k]  → O(n)
  Ex 2: two pointer — slow pointer marks next unique position
  Ex 3: merge from Day 01's merge sort — O(n+m)
  Ex 4: return n*(n+1)//2 - sum(arr)  → O(n) time, O(1) space
""")

print("═" * 57)
print("Day 02 complete. Next: Day 03 — Linked Lists")
print("═" * 57)