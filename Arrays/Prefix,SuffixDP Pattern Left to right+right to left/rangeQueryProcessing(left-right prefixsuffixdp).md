# ⛰️ Mountain Subarray Queries

## Problem

Given an array `arr[]` and multiple queries:

```text
[l, r]
```

For each query, determine whether the subarray:

```text
arr[l...r]
```

is a **mountain array**.

A subarray is a mountain if there exists an index `k` such that:

```text
l <= k <= r
```

and:

```text
arr[l] <= arr[l + 1] <= ... <= arr[k]
```

then:

```text
arr[k] >= arr[k + 1] >= ... >= arr[r]
```

So the pattern is:

```text
NON-DECREASING → NON-INCREASING
```

---

# 1. Understand the Mountain Shape

## Valid Mountain

```text
[2, 3, 4, 5, 4, 3, 2]
 ↑  ↑  ↑  ↓  ↓  ↓
             PEAK
```

Actually, visually:

```text
2 → 3 → 4 → 5 → 4 → 3 → 2
              ↑
             PEAK
```

The array has:

```text
Increasing part:
2 <= 3 <= 4 <= 5

Decreasing part:
5 >= 4 >= 3 >= 2
```

Therefore:

```text
Valid Mountain
```

---

# 2. Entirely Increasing Is Also Valid

```text
[1, 2, 3, 4]
```

```text
1 <= 2 <= 3 <= 4
```

This is valid.

The peak can be the last element:

```text
1 → 2 → 3 → 4
            PEAK
```

---

# 3. Entirely Decreasing Is Also Valid

```text
[5, 4, 3, 2]
```

```text
5 >= 4 >= 3 >= 2
```

This is valid.

The peak can be the first element:

```text
PEAK
  ↓
5 → 4 → 3 → 2
```

---

# 4. Equal Elements Are Allowed

The conditions are:

```text
<=
>=
```

not:

```text
<
>
```

Therefore:

```text
[2, 2, 2, 2]
```

is valid.

Because:

```text
2 <= 2 <= 2 <= 2
```

and:

```text
2 >= 2 >= 2 >= 2
```

---

# 5. The Invalid Pattern

A mountain can have:

```text
UP → DOWN
```

But it cannot have:

```text
DOWN → UP
```

Example:

```text
[3, 2, 4]
 ↓  ↑
```

This is invalid.

Why?

Because:

```text
3 → 2
```

is decreasing, but then:

```text
2 → 4
```

increases again.

So the array has:

```text
DECREASE → INCREASE
```

which is not a mountain.

---

# 6. Brute-Force Thinking

For every query:

```text
[l, r]
```

we can try every possible peak.

Example:

```text
arr = [2, 3, 4, 3, 2]
       0  1  2  3  4
```

Query:

```text
[0, 4]
```

Possible peaks:

```text
k = 0
k = 1
k = 2
k = 3
k = 4
```

Try:

```text
k = 2
```

Check the left side:

```text
2 <= 3 <= 4
```

Check the right side:

```text
4 >= 3 >= 2
```

Therefore:

```text
true
```

But this can be slow.

If:

```text
n = 100000
q = 100000
```

checking every element for every query can approach:

```text
O(n × q)
```

We want:

```text
Preprocessing: O(n)

Each query: O(1)

Total: O(n + q)
```

---

# 7. Core Observation

For every query:

```text
[l, r]
```

we need to find a peak:

```text
k
```

such that:

```text
l <= k <= r
```

and:

```text
l → k
```

is non-decreasing:

```text
arr[l] <= arr[l+1] <= ... <= arr[k]
```

and:

```text
k → r
```

is non-increasing:

```text
arr[k] >= arr[k+1] >= ... >= arr[r]
```

Visual:

```text
l                    k                    r
|--------------------|--------------------|
   NON-DECREASING       NON-INCREASING
```

Therefore, the real problem is:

> For every index, know how far the increasing and decreasing sequences can extend.

This leads to preprocessing arrays.

---

# 8. The `inc[]` Array

We define:

```text
inc[i] = the farthest index reachable starting from i
         while the array remains non-decreasing
```

In simple words:

> If I start at index `i`, how far right can I go while values keep increasing or staying equal?

Example:

```text
arr = [2, 3, 4, 5, 4, 3, 2]
       0  1  2  3  4  5  6
```

Starting at index `0`:

```text
2 <= 3 <= 4 <= 5
```

But:

```text
5 <= 4 ❌
```

Therefore:

```text
inc[0] = 3
```

Starting at index `1`:

```text
3 <= 4 <= 5
```

So:

```text
inc[1] = 3
```

Starting at index `2`:

```text
4 <= 5
```

So:

```text
inc[2] = 3
```

Starting at index `3`:

```text
5 <= 4 ❌
```

So:

```text
inc[3] = 3
```

Starting at index `4`:

```text
4 <= 3 ❌
```

So:

```text
inc[4] = 4
```

Starting at index `5`:

```text
3 <= 2 ❌
```

So:

```text
inc[5] = 5
```

Index `6` has no next element:

```text
inc[6] = 6
```

Final:

```text
inc = [3, 3, 3, 3, 4, 5, 6]
```

---

# 9. Important Question

Why do we calculate `inc[]` from right to left?

At first, it feels like we should do:

```text
left → right
```

because we are asking:

```text
Starting from i, how far can I go to the RIGHT?
```

That thinking is correct.

However, our recurrence is:

```text
inc[i] = inc[i + 1]
```

So:

```text
inc[i]
```

depends on:

```text
inc[i + 1]
```

Therefore, `inc[i + 1]` must already be calculated.

That means:

```text
i + 1
```

must be processed before:

```text
i
```

Therefore:

```text
RIGHT → LEFT
```

---

# 10. Deriving the `inc[]` Recurrence

Suppose:

```text
arr[i] <= arr[i + 1]
```

Example:

```text
arr[i]     = 3
arr[i + 1] = 4
```

If index `i` can move to index `i + 1`, then:

```text
inc[i] = inc[i + 1]
```

Example:

```text
arr = [2, 3, 4, 5]
       0  1  2  3
```

We already know:

```text
inc[1] = 3
```

because:

```text
3 <= 4 <= 5
```

Now:

```text
arr[0] <= arr[1]
2 <= 3
```

Therefore:

```text
inc[0] = inc[1]
```

So:

```text
inc[0] = 3
```

Because:

```text
2 <= 3 <= 4 <= 5
```

---

## If the condition fails

Suppose:

```text
arr[i] > arr[i + 1]
```

Example:

```text
5 > 4
```

Then the non-decreasing sequence stops immediately.

Therefore:

```text
inc[i] = i
```

So the recurrence is:

```python
if arr[i] <= arr[i + 1]:
    inc[i] = inc[i + 1]
else:
    inc[i] = i
```

---

# 11. Full `inc[]` Code

```python
inc = [0] * n

inc[n - 1] = n - 1

for i in range(n - 2, -1, -1):

    if arr[i] <= arr[i + 1]:
        inc[i] = inc[i + 1]

    else:
        inc[i] = i
```

---

# 12. `inc[]` Dry Run

Consider:

```text
arr = [2, 3, 4, 5, 4, 3, 2]
       0  1  2  3  4  5  6
```

Initially:

```python
inc = [0, 0, 0, 0, 0, 0, 0]
```

Set the last index:

```python
inc[6] = 6
```

Why?

Because there is no element after index `6`.

```text
inc = [0, 0, 0, 0, 0, 0, 6]
```

---

## `i = 5`

```text
arr[5] = 3
arr[6] = 2
```

Check:

```text
3 <= 2 ❌
```

Therefore:

```text
inc[5] = 5
```

```text
inc = [0, 0, 0, 0, 0, 5, 6]
```

---

## `i = 4`

```text
arr[4] = 4
arr[5] = 3
```

```text
4 <= 3 ❌
```

Therefore:

```text
inc[4] = 4
```

```text
inc = [0, 0, 0, 0, 4, 5, 6]
```

---

## `i = 3`

```text
arr[3] = 5
arr[4] = 4
```

```text
5 <= 4 ❌
```

Therefore:

```text
inc[3] = 3
```

```text
inc = [0, 0, 0, 3, 4, 5, 6]
```

---

## `i = 2`

```text
arr[2] = 4
arr[3] = 5
```

```text
4 <= 5 ✅
```

Therefore:

```text
inc[2] = inc[3]
```

```text
inc[2] = 3
```

```text
inc = [0, 0, 3, 3, 4, 5, 6]
```

---

## `i = 1`

```text
arr[1] = 3
arr[2] = 4
```

```text
3 <= 4 ✅
```

Therefore:

```text
inc[1] = inc[2]
```

```text
inc[1] = 3
```

```text
inc = [0, 3, 3, 3, 4, 5, 6]
```

---

## `i = 0`

```text
arr[0] = 2
arr[1] = 3
```

```text
2 <= 3 ✅
```

Therefore:

```text
inc[0] = inc[1]
```

```text
inc[0] = 3
```

Final:

```text
inc = [3, 3, 3, 3, 4, 5, 6]
```

---

# 13. Understanding the `inc[]` Output

```text
inc = [3, 3, 3, 3, 4, 5, 6]
```

Interpretation:

```text
inc[0] = 3
```

means:

```text
Starting at index 0,
we can go until index 3
while maintaining non-decreasing order.
```

That subarray is:

```text
arr[0...3] = [2, 3, 4, 5]
```

---

```text
inc[1] = 3
```

means:

```text
arr[1...3] = [3, 4, 5]
```

is non-decreasing.

---

```text
inc[4] = 4
```

means:

```text
Starting from index 4,
we cannot move to index 5
because:

4 <= 3 ❌
```

So the maximum reachable index is itself:

```text
4
```

---

# 14. The `dec[]` Array

Now we need the other half.

We define:

```text
dec[i] = the farthest index reachable while moving LEFT
         in non-increasing order
```

Another way to say it:

> If I want to reach index `i` through a non-increasing sequence, how far left can that sequence start?

Example:

```text
arr = [2, 3, 4, 5, 4, 3, 2]
       0  1  2  3  4  5  6
```

The decreasing sequence is:

```text
5 >= 4 >= 3 >= 2
```

It starts at index `3`.

Therefore:

```text
dec[6] = 3
```

Similarly:

```text
dec[5] = 3
dec[4] = 3
dec[3] = 3
```

The final array is:

```text
dec = [0, 1, 2, 3, 3, 3, 3]
```

---

# 15. Deriving the `dec[]` Recurrence

We scan from left to right.

Suppose:

```text
arr[i - 1] >= arr[i]
```

Example:

```text
5 >= 4
```

Then the non-increasing sequence continues.

So:

```text
dec[i] = dec[i - 1]
```

Example:

```text
arr = [5, 4, 3, 2]
       0  1  2  3
```

We know:

```text
dec[1] = 0
```

because:

```text
5 >= 4
```

Now:

```text
4 >= 3
```

So:

```text
dec[2] = dec[1]
```

Therefore:

```text
dec[2] = 0
```

The sequence still starts at index `0`.

---

## If the condition fails

Suppose:

```text
arr[i - 1] < arr[i]
```

Example:

```text
3 < 4
```

Then the decreasing sequence cannot continue from the previous index.

Therefore:

```text
dec[i] = i
```

So:

```python
if arr[i - 1] >= arr[i]:
    dec[i] = dec[i - 1]
else:
    dec[i] = i
```

---

# 16. Full `dec[]` Code

```python
dec = [0] * n

dec[0] = 0

for i in range(1, n):

    if arr[i - 1] >= arr[i]:
        dec[i] = dec[i - 1]

    else:
        dec[i] = i
```

---

# 17. `dec[]` Dry Run

```text
arr = [2, 3, 4, 5, 4, 3, 2]
       0  1  2  3  4  5  6
```

Initially:

```text
dec[0] = 0
```

---

## `i = 1`

```text
arr[0] = 2
arr[1] = 3
```

Check:

```text
2 >= 3 ❌
```

So:

```text
dec[1] = 1
```

---

## `i = 2`

```text
arr[1] = 3
arr[2] = 4
```

```text
3 >= 4 ❌
```

So:

```text
dec[2] = 2
```

---

## `i = 3`

```text
arr[2] = 4
arr[3] = 5
```

```text
4 >= 5 ❌
```

So:

```text
dec[3] = 3
```

---

## `i = 4`

```text
arr[3] = 5
arr[4] = 4
```

```text
5 >= 4 ✅
```

Therefore:

```text
dec[4] = dec[3]
```

```text
dec[4] = 3
```

---

## `i = 5`

```text
arr[4] = 4
arr[5] = 3
```

```text
4 >= 3 ✅
```

Therefore:

```text
dec[5] = dec[4]
```

```text
dec[5] = 3
```

---

## `i = 6`

```text
arr[5] = 3
arr[6] = 2
```

```text
3 >= 2 ✅
```

Therefore:

```text
dec[6] = dec[5]
```

```text
dec[6] = 3
```

Final:

```text
dec = [0, 1, 2, 3, 3, 3, 3]
```

---

# 18. Understanding the `dec[]` Output

```text
dec[6] = 3
```

means:

```text
The longest non-increasing sequence ending at index 6
starts at index 3.
```

That sequence is:

```text
arr[3...6] = [5, 4, 3, 2]
```

---

```text
dec[5] = 3
```

means:

```text
arr[3...5] = [5, 4, 3]
```

is non-increasing.

---

# 19. Query Logic

For a query:

```text
[l, r]
```

we need to find whether an increasing section from `l` and a decreasing section ending at `r` can meet.

The increasing section from `l` can go until:

```text
inc[l]
```

The decreasing section ending at `r` starts from:

```text
dec[r]
```

So we have:

```text
Increasing part:
l ---------------- inc[l]

Decreasing part:
          dec[r] ---------------- r
```

For the two parts to form a mountain, they must overlap or touch:

```text
inc[l] >= dec[r]
```

Therefore:

```python
if inc[l] >= dec[r]:
    True
else:
    False
```

---

# 20. Query Dry Run

Consider:

```text
arr = [2, 3, 4, 5, 4, 3, 2]
       0  1  2  3  4  5  6
```

We calculated:

```text
inc = [3, 3, 3, 3, 4, 5, 6]
dec = [0, 1, 2, 3, 3, 3, 3]
```

---

## Query `[0, 6]`

Increasing part from `0`:

```text
inc[0] = 3
```

So:

```text
0 → 1 → 2 → 3
```

is non-decreasing.

Decreasing part ending at `6`:

```text
dec[6] = 3
```

So:

```text
3 → 4 → 5 → 6
```

is non-increasing.

They meet at:

```text
3
```

Check:

```text
inc[0] >= dec[6]

3 >= 3
```

Therefore:

```text
true
```

---

## Query `[1, 6]`

```text
inc[1] = 3
dec[6] = 3
```

Check:

```text
3 >= 3
```

Therefore:

```text
true
```

The mountain is:

```text
3 → 4 → 5 → 4 → 3 → 2
          PEAK
```

---

## Query `[0, 3]`

```text
inc[0] = 3
dec[3] = 3
```

Check:

```text
3 >= 3
```

True.

The subarray is:

```text
[2, 3, 4, 5]
```

Entirely non-decreasing.

Still valid.

---

## Query `[3, 6]`

```text
inc[3] = 3
dec[6] = 3
```

Check:

```text
3 >= 3
```

True.

The subarray is:

```text
[5, 4, 3, 2]
```

Entirely non-increasing.

Still valid.

---

# 21. Invalid Query Example

Consider:

```text
arr = [3, 2, 4]
       0  1  2
```

Calculate `inc[]`.

At index `0`:

```text
3 <= 2 ❌
```

Therefore:

```text
inc[0] = 0
```

Calculate `dec[]`.

For index `2`:

```text
arr[1] >= arr[2]
2 >= 4 ❌
```

Therefore:

```text
dec[2] = 2
```

Now query:

```text
[0, 2]
```

Check:

```text
inc[0] >= dec[2]

0 >= 2
```

False.

Therefore:

```text
[3, 2, 4]
```

is not a mountain.

---

# 22. Complete Code

```python
def mountain_queries(arr, queries):

    n = len(arr)

    # --------------------------------------------------
    # inc[i] =
    # farthest index reachable from i
    # while the array is non-decreasing
    # --------------------------------------------------

    inc = [0] * n

    inc[n - 1] = n - 1

    for i in range(n - 2, -1, -1):

        if arr[i] <= arr[i + 1]:
            inc[i] = inc[i + 1]

        else:
            inc[i] = i

    # --------------------------------------------------
    # dec[i] =
    # farthest left index from which we can reach i
    # while the array is non-increasing
    # --------------------------------------------------

    dec = [0] * n

    dec[0] = 0

    for i in range(1, n):

        if arr[i - 1] >= arr[i]:
            dec[i] = dec[i - 1]

        else:
            dec[i] = i

    # --------------------------------------------------
    # Answer queries
    # --------------------------------------------------

    ans = []

    for l, r in queries:

        if inc[l] >= dec[r]:
            ans.append(True)

        else:
            ans.append(False)

    return ans
```

---

# 23. Complete Example

```python
arr = [2, 3, 2, 4, 4, 6, 3, 2]

queries = [
    [0, 2],
    [1, 3]
]
```

Array:

```text
index:  0  1  2  3  4  5  6  7
arr:    2  3  2  4  4  6  3  2
```

---

## Build `inc[]`

```text
inc = [1, 1, 5, 5, 5, 5, 6, 7]
```

Interpretation:

```text
inc[0] = 1
```

because:

```text
2 <= 3
```

but:

```text
3 <= 2 ❌
```

---

## Build `dec[]`

```text
dec = [0, 1, 2, 3, 3, 5, 6, 6]
```

Interpretation:

```text
dec[6] = 6
```

because:

```text
3 >= 2
```

and the sequence ending at index `6` starts at index `6`.

For index `7`:

```text
3 >= 2
```

Therefore:

```text
dec[7] = 6
```

---

## Query `[0, 2]`

```text
inc[0] = 1
dec[2] = 2
```

Check:

```text
1 >= 2
```

False?

But the subarray is:

```text
[2, 3, 2]
```

which is clearly a mountain.

This reveals an important issue in the interpretation of the arrays.

The cleanest implementation should instead use:

```text
upEnd[i] = farthest right index reachable from i
           while non-decreasing

downStart[i] = farthest left index reachable from i
               while non-increasing
```

Then for query `[l, r]`:

```text
upEnd[l] >= downStart[r]
```

For:

```text
[2, 3, 2]
```

we have:

```text
upEnd[0] = 1
downStart[2] = 1
```

Therefore:

```text
1 >= 1
```

True.

---

# 24. Correct Interpretation of the Two Arrays

Use these definitions:

## `upEnd[i]`

```text
upEnd[i] =
the farthest index to the RIGHT reachable from i
while:

arr[i] <= arr[i+1] <= ...
```

Example:

```text
[2, 3, 4, 5, 4]
```

Then:

```text
upEnd[0] = 3
```

because:

```text
2 <= 3 <= 4 <= 5
```

---

## `downStart[i]`

```text
downStart[i] =
the farthest index to the LEFT reachable from i
while:

arr[start] >= ... >= arr[i]
```

Example:

```text
[2, 3, 4, 5, 4, 3, 2]
```

Then:

```text
downStart[6] = 3
```

because:

```text
5 >= 4 >= 3 >= 2
```

---

# 25. The Most Important Query Formula

For query:

```text
[l, r]
```

we need:

```text
upEnd[l] >= downStart[r]
```

Why?

Because:

```text
Increasing part:
l ------------ upEnd[l]

Decreasing part:
        downStart[r] ------------ r
```

If:

```text
upEnd[l] >= downStart[r]
```

then the two parts overlap.

Therefore, a peak exists.

---

# 26. Correct Code Using These Definitions

```python
def is_mountain_queries(arr, queries):

    n = len(arr)

    # upEnd[i]:
    # farthest right index reachable from i
    # while non-decreasing

    upEnd = [0] * n

    upEnd[n - 1] = n - 1

    for i in range(n - 2, -1, -1):

        if arr[i] <= arr[i + 1]:
            upEnd[i] = upEnd[i + 1]

        else:
            upEnd[i] = i

    # downStart[i]:
    # farthest left index reachable from i
    # while non-increasing

    downStart = [0] * n

    downStart[0] = 0

    for i in range(1, n):

        if arr[i - 1] >= arr[i]:
            downStart[i] = downStart[i - 1]

        else:
            downStart[i] = i

    ans = []

    for l, r in queries:

        if upEnd[l] >= downStart[r]:
            ans.append(True)
        else:
            ans.append(False)

    return ans
```

---

# 27. Important DP Direction Pattern

This problem teaches a very important general rule.

Suppose:

```text
dp[i] depends on dp[i + 1]
```

Then calculate:

```text
RIGHT → LEFT
```

Example:

```python
inc[i] = inc[i + 1]
```

Therefore:

```python
for i in range(n - 2, -1, -1):
```

---

Suppose:

```text
dp[i] depends on dp[i - 1]
```

Then calculate:

```text
LEFT → RIGHT
```

Example:

```python
dec[i] = dec[i - 1]
```

Therefore:

```python
for i in range(1, n):
```

---

# 28. The General Rule

Do not decide loop direction based only on the English meaning.

Instead ask:

> What previous state does my current state depend on?

If:

```text
current = future
```

then:

```text
RIGHT → LEFT
```

If:

```text
current = previous
```

then:

```text
LEFT → RIGHT
```

Table:

| Recurrence          | Direction    |
| ------------------- | ------------ |
| `dp[i] = dp[i - 1]` | Left → Right |
| `dp[i] = dp[i + 1]` | Right → Left |

This appears everywhere in:

* Dynamic Programming
* Prefix/suffix preprocessing
* Reachability arrays
* Monotonic runs
* Next greater/smaller preprocessing
* Suffix maximum/minimum arrays

---

# 29. Pattern Name

This problem belongs to the pattern:

## Range Query Preprocessing on Monotonic Runs

It also uses:

```text
Directional DP
```

and:

```text
Left/Right Reachability Preprocessing
```

The general structure is:

```text
Precompute local property
        ↓
Build reachability information
        ↓
Answer each range query in O(1)
```

---

# 30. Pattern Recognition Checklist

When you see:

```text
Given an array
Given many [l, r] queries
Ask whether each subarray satisfies some property
```

ask:

### Question 1

Can the property be represented as a continuous run?

Examples:

```text
non-decreasing
non-increasing
same parity
same color
same difference
```

If yes:

```text
Precompute run boundaries.
```

---

### Question 2

Can I calculate:

```text
farthest reachable index from i
```

If yes:

```text
Build a reachability array.
```

---

### Question 3

Does the current state depend on:

```text
i - 1
```

Then:

```text
left → right
```

Does it depend on:

```text
i + 1
```

Then:

```text
right → left
```

---

### Question 4

Can the query be answered using two boundaries?

For this problem:

```text
increasing range from l
```

and:

```text
decreasing range ending at r
```

If they overlap:

```text
valid
```

---

# 31. General Template

```python
n = len(arr)

leftReach = [0] * n

# If current state depends on i + 1:
for i in range(n - 2, -1, -1):

    if condition_with_next_element:

        leftReach[i] = leftReach[i + 1]

    else:

        leftReach[i] = i


rightReach = [0] * n

# If current state depends on i - 1:
for i in range(1, n):

    if condition_with_previous_element:

        rightReach[i] = rightReach[i - 1]

    else:

        rightReach[i] = i


for l, r in queries:

    # Compare the two reachable boundaries

    if leftReach[l] >= rightReach[r]:

        answer = True

    else:

        answer = False
```

---

# 32. Similar Problems

This pattern is useful for problems involving:

## 1. Non-decreasing subarray queries

Question:

```text
Is arr[l...r] non-decreasing?
```

Precompute:

```text
end of increasing run
```

Then:

```text
endIncreasing[l] >= r
```

---

## 2. Non-increasing subarray queries

Question:

```text
Is arr[l...r] non-increasing?
```

Precompute:

```text
start of decreasing run
```

Then:

```text
startDecreasing[r] <= l
```

---

## 3. Good Days to Rob the Bank

The condition is:

```text
previous time days are non-increasing
```

and:

```text
next time days are non-decreasing
```

This is also:

```text
LEFT CONDITION + RIGHT CONDITION
```

---

## 4. Longest Bitonic Subarray

A bitonic array is:

```text
increasing → decreasing
```

The same mountain idea appears.

Instead of answering queries, we maximize:

```text
length
```

---

## 5. Longest Mountain in Array

Again:

```text
increasing → decreasing
```

Usually solved with:

```text
up[] + down[]
```

or two-pointer traversal.

---

## 6. Range queries with sorted segments

If a query asks:

```text
Is this range sorted?
```

you can precompute:

```text
last position where order was violated
```

Then answer each query in:

```text
O(1)
```

---

# 33. Real-World Analogy

Imagine a road.

A mountain road has:

```text
Start → climb → peak → descend → end
```

For every query asking:

```text
From point l to point r,
is the road a mountain?
```

we precompute:

```text
From each point:
How far can I continue climbing?
```

and:

```text
For each point:
How far back does the current descending road extend?
```

Then we check:

```text
Does the climbing route and descending route meet?
```

If yes:

```text
Mountain.
```

---

# 34. Interview Quick Revision Sheet

## Problem Pattern

```text
Many range queries
+
Monotonic property
```

Think:

```text
Precompute monotonic runs.
```

---

## Mountain Definition

```text
NON-DECREASING → NON-INCREASING
```

Allowed:

```text
UP
UP → DOWN
DOWN
```

Not allowed:

```text
DOWN → UP
```

---

## Increasing Array

```text
upEnd[i]
```

Meaning:

```text
Farthest right index reachable from i
while arr is non-decreasing.
```

Condition:

```python
arr[i] <= arr[i + 1]
```

Recurrence:

```python
upEnd[i] = upEnd[i + 1]
```

Direction:

```text
RIGHT → LEFT
```

---

## Decreasing Array

```text
downStart[i]
```

Meaning:

```text
Farthest left index reachable from i
while arr is non-increasing.
```

Condition:

```python
arr[i - 1] >= arr[i]
```

Recurrence:

```python
downStart[i] = downStart[i - 1]
```

Direction:

```text
LEFT → RIGHT
```

---

## Query

For:

```text
[l, r]
```

check:

```python
upEnd[l] >= downStart[r]
```

If true:

```text
Mountain
```

Otherwise:

```text
Not Mountain
```

---

## Complexity

Preprocessing:

```text
O(n)
```

Each query:

```text
O(1)
```

Total:

```text
O(n + q)
```

Space:

```text
O(n)
```

---

# 35. The Most Important Mental Model

Do not memorize:

```python
for i in range(n - 2, -1, -1)
```

Instead memorize the dependency:

```text
inc[i] depends on inc[i + 1]
```

Therefore:

```text
calculate i + 1 first
```

Therefore:

```text
RIGHT → LEFT
```

Similarly:

```text
dec[i] depends on dec[i - 1]
```

Therefore:

```text
calculate i - 1 first
```

Therefore:

```text
LEFT → RIGHT
```

The ultimate rule is:

> **The loop direction is determined by the dependency, not by the name of the array.**

---

# Final Pattern

```text
Many range queries
        ↓
Property is based on continuous monotonic segments
        ↓
Precompute farthest reachable boundaries
        ↓
For each [l, r], compare the boundaries
        ↓
O(n + q)
```

For mountain queries:

```text
Increasing from l
        +
Decreasing toward r
        ↓
Do they overlap?
        ↓
Yes → Mountain
No  → Not Mountain
```

This is the core idea to remember.
