# Maximum Sum of 3 Non-Overlapping Subarrays

## Problem

Given an integer array `nums` and an integer `k`, find three non-overlapping contiguous subarrays, each of length `k`, such that their total sum is maximum.

### Example

~~~text
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
~~~

One possible selection is:

~~~text
[1, 2] | [6, 7] | [5, 1]
~~~

Their sums are:

~~~text
3 + 13 + 6 = 22
~~~

The starting indices are:

~~~text
[0, 4, 6]
~~~

---

# 1. Logic Building

We need to choose exactly three non-overlapping subarrays:

~~~text
LEFT | MIDDLE | RIGHT
~~~

Each subarray has exactly length `k`.

Therefore:

~~~text
best left window
+
current middle window
+
best right window
~~~

The main question is:

> For every possible middle window, what is the best valid window before it and after it?

---

# 2. Step 1: Create All Fixed-Length Window Sums

Given:

~~~text
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
~~~

All windows of length `2` are:

~~~text
Window 0 → nums[0:2] → [1, 2] → 3
Window 1 → nums[1:3] → [2, 1] → 3
Window 2 → nums[2:4] → [1, 2] → 3
Window 3 → nums[3:5] → [2, 6] → 8
Window 4 → nums[4:6] → [6, 7] → 13
Window 5 → nums[5:7] → [7, 5] → 12
Window 6 → nums[6:8] → [5, 1] → 6
~~~

Therefore:

~~~text
window_sum = [3, 3, 3, 8, 13, 12, 6]
~~~

Number of windows:

~~~text
n - k + 1
~~~

For:

~~~text
n = 8
k = 2
~~~

we get:

~~~text
8 - 2 + 1 = 7
~~~

windows.

---

# 3. Window Index vs Normal Array Index

This is the most important concept.

Original array:

~~~text
Index:  0  1  2  3  4  5  6  7
Value:  1  2  1  2  6  7  5  1
~~~

Because:

~~~text
k = 2
~~~

we have:

~~~text
window[i] = nums[i : i + k]
~~~

Therefore:

~~~text
Window 0 → nums[0:2] → indices 0,1 → sum 3
Window 1 → nums[1:3] → indices 1,2 → sum 3
Window 2 → nums[2:4] → indices 2,3 → sum 3
Window 3 → nums[3:5] → indices 3,4 → sum 8
Window 4 → nums[4:6] → indices 4,5 → sum 13
Window 5 → nums[5:7] → indices 5,6 → sum 12
Window 6 → nums[6:8] → indices 6,7 → sum 6
~~~

Mapping:

~~~text
Window Index:  0      1      2      3      4      5      6
Window Sum:    3      3      3      8     13     12      6

Array Indices: 0,1    1,2    2,3    3,4    4,5    5,6    6,7
~~~

The important formula is:

~~~text
window[i] = nums[i : i + k]
~~~

For example:

~~~text
window[3] = nums[3:5]
~~~

This means:

~~~text
nums[3] and nums[4]
~~~

Therefore:

~~~text
window index 3
~~~

represents the original array subarray:

~~~text
[2, 6]
~~~

---

# 4. Choosing a Middle Window

Suppose:

~~~text
middle = 3
~~~

Then:

~~~text
window[3] = nums[3:5] = [2, 6]
~~~

It occupies normal array indices:

~~~text
3, 4
~~~

We need:

~~~text
LEFT | MIDDLE | RIGHT
~~~

## Left Side

The left window must not overlap with array indices `3` or `4`.

Check:

~~~text
Window 2 → indices 2,3 → overlaps ❌
Window 1 → indices 1,2 → valid ✅
Window 0 → indices 0,1 → valid ✅
~~~

Therefore:

~~~text
valid left windows = [0, 1]
~~~

## Right Side

The right window must not overlap with array indices `3` or `4`.

Check:

~~~text
Window 4 → indices 4,5 → overlaps ❌
Window 5 → indices 5,6 → valid ✅
Window 6 → indices 6,7 → valid ✅
~~~

Therefore:

~~~text
valid right windows = [5, 6]
~~~

So:

~~~text
LEFT       MIDDLE       RIGHT
[0,1]       [3]         [5,6]
~~~

---

# 5. Deriving the Boundary Formula

Suppose:

~~~text
middle = i
k = window length
~~~

The middle window is:

~~~text
nums[i : i + k]
~~~

It occupies:

~~~text
i, i + 1, ..., i + k - 1
~~~

## Left Boundary

The latest possible left window starts at:

~~~text
i - k
~~~

Therefore:

~~~text
left window index <= i - k
~~~

## Right Boundary

The earliest possible right window starts at:

~~~text
i + k
~~~

Therefore:

~~~text
right window index >= i + k
~~~

So the formula is:

~~~text
left  <= middle - k
right >= middle + k
~~~

For:

~~~text
middle = 3
k = 2
~~~

we get:

~~~text
left <= 3 - 2 = 1
right >= 3 + 2 = 5
~~~

Therefore:

~~~text
left windows  = [0, 1]
middle        = [3]
right windows = [5, 6]
~~~

---

# 6. What Do We Precompute?

For every window, we want to quickly know:

~~~text
What is the best window from the beginning up to this position?
~~~

and:

~~~text
What is the best window from this position until the end?
~~~

So we create:

~~~text
left_best[i]
right_best[i]
~~~

These arrays store the INDEX of the best window.

They do not store the actual sum.

---

# 7. Building `left_best`

Definition:

~~~text
left_best[i]
~~~

stores the index of the maximum-sum window among:

~~~text
window[0 ... i]
~~~

Given:

~~~text
window_sum = [3, 3, 3, 8, 13, 12, 6]
~~~

Scan from left to right.

~~~text
i = 0
range = [3]
best index = 0
~~~

~~~text
i = 1
range = [3, 3]
best index = 0
~~~

When sums are equal, we keep the earlier index.

~~~text
i = 2
range = [3, 3, 3]
best index = 0
~~~

~~~text
i = 3
range = [3, 3, 3, 8]
best index = 3
~~~

~~~text
i = 4
range = [3, 3, 3, 8, 13]
best index = 4
~~~

~~~text
i = 5
range = [3, 3, 3, 8, 13, 12]
best index = 4
~~~

~~~text
i = 6
range = [3, 3, 3, 8, 13, 12, 6]
best index = 4
~~~

Therefore:

~~~text
left_best = [0, 0, 0, 3, 4, 4, 4]
~~~

For example:

~~~text
left_best[2] = 0
~~~

means:

> Among windows `0, 1, 2`, the best window is window `0`.

And:

~~~text
left_best[5] = 4
~~~

means:

> Among windows `0, 1, 2, 3, 4, 5`, the best window is window `4`.

The code:

~~~python
left_best = [0] * m

best_index = 0

for i in range(m):

    if window_sum[i] > window_sum[best_index]:
        best_index = i

    left_best[i] = best_index
~~~

---

# 8. Building `right_best`

Definition:

~~~text
right_best[i]
~~~

stores the index of the maximum-sum window among:

~~~text
window[i ... end]
~~~

We scan from right to left.

Given:

~~~text
window_sum = [3, 3, 3, 8, 13, 12, 6]
~~~

Start from the right:

~~~text
i = 6
range = [6]
best index = 6
~~~

~~~text
i = 5
range = [12, 6]
best index = 5
~~~

~~~text
i = 4
range = [13, 12, 6]
best index = 4
~~~

~~~text
i = 3
range = [8, 13, 12, 6]
best index = 4
~~~

~~~text
i = 2
best index = 4
~~~

~~~text
i = 1
best index = 4
~~~

~~~text
i = 0
best index = 4
~~~

Therefore:

~~~text
right_best = [4, 4, 4, 4, 4, 5, 6]
~~~

The code:

~~~python
right_best = [0] * m

best_index = m - 1

for i in range(m - 1, -1, -1):

    if window_sum[i] >= window_sum[best_index]:
        best_index = i

    right_best[i] = best_index
~~~

---

# 9. Try Every Possible Middle Window

For every possible middle window:

~~~text
middle = i
~~~

we choose:

~~~text
left = left_best[i - k]
~~~

and:

~~~text
right = right_best[i + k]
~~~

Then:

~~~text
total =
window_sum[left]
+
window_sum[middle]
+
window_sum[right]
~~~

Why?

Because:

~~~text
left <= i - k
~~~

and:

~~~text
right >= i + k
~~~

guarantee that the three windows are non-overlapping.

---

# 10. Complete Dry Run

We have:

~~~text
window_sum = [3, 3, 3, 8, 13, 12, 6]
k = 2
~~~

And:

~~~text
left_best  = [0, 0, 0, 3, 4, 4, 4]
right_best = [4, 4, 4, 4, 4, 5, 6]
~~~

---

## Middle = 2

Middle:

~~~text
window[2] = 3
~~~

Left:

~~~text
left_best[2 - 2]
= left_best[0]
= 0
~~~

Right:

~~~text
right_best[2 + 2]
= right_best[4]
= 4
~~~

Total:

~~~text
window_sum[0] + window_sum[2] + window_sum[4]
~~~

~~~text
3 + 3 + 13 = 19
~~~

Selected windows:

~~~text
Window 0 | Window 2 | Window 4
~~~

Original array:

~~~text
[1, 2] | [1, 2] | [6, 7]
~~~

---

## Middle = 3

Middle:

~~~text
window[3] = 8
~~~

Left:

~~~text
left_best[3 - 2]
= left_best[1]
= 0
~~~

Right:

~~~text
right_best[3 + 2]
= right_best[5]
= 5
~~~

Total:

~~~text
window_sum[0] + window_sum[3] + window_sum[5]
~~~

~~~text
3 + 8 + 12 = 23
~~~

Selected windows:

~~~text
Window 0 | Window 3 | Window 5
~~~

Original array indices:

~~~text
[0,1] | [3,4] | [5,6]
~~~

Original subarrays:

~~~text
[1, 2] | [2, 6] | [7, 5]
~~~

Total:

~~~text
3 + 8 + 12 = 23
~~~

---

## Middle = 4

Middle:

~~~text
window[4] = 13
~~~

Left:

~~~text
left_best[4 - 2]
= left_best[2]
= 0
~~~

Right:

~~~text
right_best[4 + 2]
= right_best[6]
= 6
~~~

Total:

~~~text
window_sum[0] + window_sum[4] + window_sum[6]
~~~

~~~text
3 + 13 + 6 = 22
~~~

Selected windows:

~~~text
Window 0 | Window 4 | Window 6
~~~

Original array:

~~~text
[1, 2] | [6, 7] | [5, 1]
~~~

Total:

~~~text
3 + 13 + 6 = 22
~~~

---

# 11. Why Do We Start the Middle Loop at `k`?

We need one complete window before the middle.

If:

~~~text
middle < k
~~~

there is not enough space for a previous non-overlapping window.

Therefore:

~~~python
for middle in range(k, ...):
~~~

For:

~~~text
k = 2
~~~

the first possible middle is:

~~~text
middle = 2
~~~

because:

~~~text
Window 0 | Window 2
~~~

is valid.

---

# 12. Why Do We Stop at `m - k`?

We need one complete window after the middle.

Therefore:

~~~text
middle + k < m
~~~

which means:

~~~text
middle < m - k
~~~

So the loop is:

~~~python
for middle in range(k, m - k):
~~~

For:

~~~text
m = 7
k = 2
~~~

the middle indices are:

~~~text
2, 3, 4
~~~

Exactly the valid possibilities.

---

# 13. Sliding Window to Build `window_sum`

Instead of calculating every window sum from scratch, use a sliding window.

For:

~~~text
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
~~~

First window:

~~~text
[1, 2]
~~~

Sum:

~~~text
3
~~~

Move one position right:

~~~text
[1, 2] → [2, 1]
~~~

Remove:

~~~text
1
~~~

Add:

~~~text
1
~~~

New sum:

~~~text
3
~~~

Move again:

~~~text
[2, 1] → [1, 2]
~~~

Remove:

~~~text
2
~~~

Add:

~~~text
2
~~~

New sum:

~~~text
3
~~~

The formula is:

~~~text
new_sum = old_sum
         - nums[i-k]
         + nums[i]
~~~

Code:

~~~python
window_sum = [0] * (n - k + 1)

current = sum(nums[:k])
window_sum[0] = current

for i in range(k, n):

    current += nums[i]
    current -= nums[i - k]

    window_sum[i - k + 1] = current
~~~

---

# 14. Complete Code

~~~python
def max_sum_of_three_subarrays(nums, k):

    n = len(nums)

    # ------------------------------------
    # Step 1: Calculate every window sum
    # ------------------------------------

    window_sum = [0] * (n - k + 1)

    current = sum(nums[:k])
    window_sum[0] = current

    for i in range(k, n):

        current += nums[i]
        current -= nums[i - k]

        window_sum[i - k + 1] = current

    m = len(window_sum)

    # ------------------------------------
    # Step 2: Prefix best window
    # ------------------------------------

    left_best = [0] * m

    best_index = 0

    for i in range(m):

        if window_sum[i] > window_sum[best_index]:
            best_index = i

        left_best[i] = best_index

    # ------------------------------------
    # Step 3: Suffix best window
    # ------------------------------------

    right_best = [0] * m

    best_index = m - 1

    for i in range(m - 1, -1, -1):

        if window_sum[i] >= window_sum[best_index]:
            best_index = i

        right_best[i] = best_index

    # ------------------------------------
    # Step 4: Try every middle window
    # ------------------------------------

    answer = [-1, -1, -1]
    max_total = float("-inf")

    for middle in range(k, m - k):

        left = left_best[middle - k]
        right = right_best[middle + k]

        total = (
            window_sum[left]
            + window_sum[middle]
            + window_sum[right]
        )

        if total > max_total:

            max_total = total

            answer = [
                left,
                middle,
                right
            ]

    return answer
~~~

---

# 15. Code Dry Run

For:

~~~python
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
~~~

Step 1:

~~~text
window_sum = [3, 3, 3, 8, 13, 12, 6]
~~~

Step 2:

~~~text
left_best = [0, 0, 0, 3, 4, 4, 4]
~~~

Step 3:

~~~text
right_best = [4, 4, 4, 4, 4, 5, 6]
~~~

Step 4:

For:

~~~text
middle = 2
~~~

~~~text
left = left_best[0] = 0
right = right_best[4] = 4
total = 3 + 3 + 13 = 19
~~~

For:

~~~text
middle = 3
~~~

~~~text
left = left_best[1] = 0
right = right_best[5] = 5
total = 3 + 8 + 12 = 23
~~~

For:

~~~text
middle = 4
~~~

~~~text
left = left_best[2] = 0
right = right_best[6] = 6
total = 3 + 13 + 6 = 22
~~~

Maximum:

~~~text
23
~~~

Answer:

~~~text
[0, 3, 5]
~~~

The selected subarrays are:

~~~text
nums[0:2] = [1, 2] → 3
nums[3:5] = [2, 6] → 8
nums[5:7] = [7, 5] → 12
~~~

Total:

~~~text
3 + 8 + 12 = 23
~~~

---

# 16. Important Correction About the Example

The commonly shown selection:

~~~text
[1, 2] | [6, 7] | [5, 1]
~~~

has total:

~~~text
3 + 13 + 6 = 22
~~~

But for:

~~~text
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
~~~

the better valid selection is:

~~~text
[1, 2] | [2, 6] | [7, 5]
~~~

with indices:

~~~text
[0, 3, 5]
~~~

and total:

~~~text
3 + 8 + 12 = 23
~~~

These subarrays are non-overlapping:

~~~text
[0,1] | [3,4] | [5,6]
~~~

Therefore, the maximum sum is:

~~~text
23
~~~

---

# 17. Pattern Name

## Fixed-Length Non-Overlapping Subarrays + Prefix/Suffix Best

The complete pattern is:

~~~text
Fixed-length subarrays
        ↓
Sliding Window
        ↓
Create all window sums
        ↓
Prefix Best
        +
Suffix Best
        ↓
Choose middle window
        ↓
Combine:
leftBest + middle + rightBest
~~~

This is a combination of:

1. Sliding Window
2. Prefix Dynamic Programming
3. Suffix Dynamic Programming
4. Non-overlapping Interval Selection

---

# 18. General Template

For fixed-length subarrays:

~~~text
window_sum[i] = sum of subarray starting at i
~~~

Then:

~~~text
left_best[i] =
best window index in [0 ... i]
~~~

and:

~~~text
right_best[i] =
best window index in [i ... end]
~~~

For three windows:

~~~text
for middle in valid positions:

    left = left_best[middle - k]

    right = right_best[middle + k]

    answer =
        window_sum[left]
        + window_sum[middle]
        + window_sum[right]
~~~

General structure:

~~~text
LEFT | MIDDLE | RIGHT
  ↓       ↓       ↓
best    fixed   best
left    middle  right
~~~

---

# 19. Quick Identification

When you see:

> Select multiple non-overlapping subarrays.

Ask:

### Question 1

Are the subarrays fixed length?

Yes → Sliding Window  
No  → Kadane / Prefix Sum / DP may be needed

---

### Question 2

Can the array be divided into:

LEFT | MIDDLE | RIGHT

If yes:

Precompute best answers on the left and right.

---

### Question 3

Does the middle determine the valid boundaries?

For fixed length k:

left <= middle - k  
right >= middle + k

Then:

Prefix Best + Current Middle + Suffix Best

is a strong candidate pattern.

---

## 20. Complexity

Let:

n = len(nums)

### Time Complexity

Window sums:

O(n)

Prefix best:

O(n)

Suffix best:

O(n)

Middle loop:

O(n)

Total:

O(n)

### Space Complexity

window_sum → O(n)  
left_best  → O(n)  
right_best → O(n)

Total:

O(n)

---

## 21. Real-World Analogy

Suppose a company wants to select three non-overlapping time slots for three advertisements.

Each advertisement must run for exactly k minutes.

Each time slot has a profit:

slot 0 → profit 3  
slot 1 → profit 3  
slot 2 → profit 3  
slot 3 → profit 8  
slot 4 → profit 13  
slot 5 → profit 12  
slot 6 → profit 6

For every possible middle advertisement:

best advertisement before it  
+  
current advertisement  
+  
best advertisement after it

The same algorithm finds the maximum total profit.

---

## 22. Interview Quick Revision

### Problem

Choose 3 non-overlapping subarrays of fixed length k with maximum total sum.

---

### Pattern

Sliding Window  
+  
Prefix Best  
+  
Suffix Best

---

### Steps

1. Calculate every length-k window sum.

2. Build left_best:
   best window index from 0 to i.

3. Build right_best:
   best window index from i to end.

4. Try every possible middle window.

5. Find:

   left  = left_best[middle - k]  
   right = right_best[middle + k]

6. Calculate:

   window_sum[left]  
   + window_sum[middle]  
   + window_sum[right]

7. Keep the maximum.

---

### Most Important Formula

left  = left_best[middle - k]  
right = right_best[middle + k]

---

### Why?

Because the middle window:

nums[middle : middle + k]

occupies:

middle ... middle + k - 1

Therefore:

left window must finish before middle

right window must start at or after middle + k

---

## Final Pattern

Fixed-Length Subarrays  
        ↓  
Sliding Window  
        ↓  
Window Sums  
        ↓  
Prefix Best  
        +  
Suffix Best  
        ↓  
Try Middle  
        ↓  
Best Left + Middle + Best Right  
        ↓  
Maximum Answer