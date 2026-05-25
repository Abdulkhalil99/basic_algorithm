"""
============================================================
  DSA FROM SCRATCH — Day 01: Big O Notation
============================================================

What is Big O?
--------------
Big O notation describes HOW FAST your code grows
as the input size (n) grows. It answers:

  "If my input doubles, how does my runtime change?"

We care about the WORST CASE and we DROP constants.

O(1)      → Constant   — doesn't matter how big n is
O(log n)  → Logarithmic — doubles input = +1 step
O(n)      → Linear     — doubles input = double the steps
O(n log n)→ Log-linear — fast sorts (merge sort, etc.)
O(n²)     → Quadratic  — doubles input = 4x the steps
O(2ⁿ)     → Exponential— adds 1 to input = double the steps

============================================================
"""


# ─────────────────────────────────────────
# O(1) — Constant Time
# ─────────────────────────────────────────
# No matter how big the list is, we always
# do ONE operation: grab index 0.

def get_first(items):
    return items[0]

# Example:
nums = [10, 20, 30, 40, 50]
print("O(1) example:", get_first(nums))   # Always 1 step


# ─────────────────────────────────────────
# O(n) — Linear Time
# ─────────────────────────────────────────
# We visit every element once.
# 5 items → 5 steps. 1000 items → 1000 steps.

def find_max(items):
    max_val = items[0]
    for item in items:          # n steps
        if item > max_val:
            max_val = item
    return max_val

print("O(n) example:", find_max(nums))    # 5 steps for 5 items


# ─────────────────────────────────────────
# O(n²) — Quadratic Time
# ─────────────────────────────────────────
# Nested loops. For every element,
# we loop through all elements again.
# 5 items → 25 steps. 100 items → 10,000 steps. Yikes.

def has_duplicate(items):
    for i in range(len(items)):           # n steps
        for j in range(len(items)):       # n steps (nested!)
            if i != j and items[i] == items[j]:
                return True
    return False

data = [1, 2, 3, 4, 5]
print("O(n²) example - has duplicate:", has_duplicate(data))   # False


# ─────────────────────────────────────────
# O(log n) — Logarithmic Time
# ─────────────────────────────────────────
# Every step, we CUT the problem in HALF.
# 1000 items → only ~10 steps!
# (Binary search — works on sorted lists)

def binary_search(items, target):
    left, right = 0, len(items) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        if items[mid] == target:
            print(f"  Found in {steps} step(s)")
            return mid
        elif items[mid] < target:
            left = mid + 1      # discard LEFT half
        else:
            right = mid - 1     # discard RIGHT half

    return -1   # not found

sorted_nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print("O(log n) example — searching for 15:")
binary_search(sorted_nums, 15)   # only 3-4 steps for 10 items!


# ─────────────────────────────────────────
# O(n log n) — Log-linear Time
# ─────────────────────────────────────────
# The best we can do for comparison-based sorting.
# Merge sort, quick sort, Python's built-in sort.

def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left  = merge_sort(items[:mid])    # split & recurse
    right = merge_sort(items[mid:])    # split & recurse

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsorted = [5, 2, 8, 1, 9, 3]
print("O(n log n) example:", merge_sort(unsorted))


# ─────────────────────────────────────────
# O(2ⁿ) — Exponential Time
# ─────────────────────────────────────────
# Avoid this unless absolutely necessary.
# Classic example: naive Fibonacci.
# fib(30) = ~1 billion operations!

def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)   # two branches each call

print("O(2ⁿ) example — fib(10):", fib_slow(10))   # Fine for small n


# ─────────────────────────────────────────
# THE GOLDEN RULE OF BIG O
# ─────────────────────────────────────────
# 1. Drop constants:  O(2n) → O(n)
# 2. Drop non-dominant terms: O(n² + n) → O(n²)
# 3. Different inputs = different variables:
#       def foo(a, b):  ← O(a + b), NOT O(n)

def demo_drop_constants(items):
    # Two separate loops = O(n) + O(n) = O(2n) → still O(n)
    for x in items: pass    # O(n)
    for x in items: pass    # O(n)

def demo_drop_nondominant(items):
    # O(n²) dominates O(n), so we call it O(n²)
    for i in items:         # O(n)
        for j in items:     # O(n²) total
            pass
    for k in items: pass    # O(n) — irrelevant next to n²


# ─────────────────────────────────────────
# QUICK REFERENCE CHEAT SHEET
# ─────────────────────────────────────────
#
#  Complexity  |  n=10   |  n=100  |  n=1000
# -------------|---------|---------|----------
#  O(1)        |   1     |   1     |   1
#  O(log n)    |   3     |   7     |   10
#  O(n)        |  10     |  100    |  1,000
#  O(n log n)  |  33     |  664    |  9,966
#  O(n²)       | 100     | 10,000  | 1,000,000
#  O(2ⁿ)       | 1,024   | huge    | astronomical
#
# ─────────────────────────────────────────
# EXERCISES (try these yourself!)
# ─────────────────────────────────────────
#
# 1. What is the Big O of this function?
#    def mystery(n):
#        count = 0
#        while n > 1:
#            n = n // 2
#            count += 1
#        return count
#    Answer: ______
#
# 2. What is the Big O of this?
#    def mystery2(items):
#        return items[-1]
#    Answer: ______
#
# 3. What is the Big O of this?
#    def mystery3(items):
#        for i in items:
#            for j in items:
#                for k in items:
#                    pass
#    Answer: ______
#
# Answers: 1) O(log n)  2) O(1)  3) O(n³)