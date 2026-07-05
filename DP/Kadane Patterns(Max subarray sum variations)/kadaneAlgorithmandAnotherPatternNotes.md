# 📘 DP Notes: Kadane's Algorithm & Maximum Subarray Sum with At Most One Deletion

---

# Part 1: Kadane's Algorithm (Maximum Subarray Sum)

---

# Problem Statement

Given an integer array `arr[]`, find the maximum sum of a **non-empty contiguous subarray**.

### Example

```python
arr = [-2,1,-3,4,-1,2,1,-5,4]
Answer = 6
Subarray = [4,-1,2,1]
```

---

# Brute Force

Generate every subarray and calculate its sum.

```python
def brute(arr):
    n = len(arr)
    ans = float('-inf')

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            ans = max(ans, s)

    return ans
```

### Complexity

```text
Time  : O(N²)
Space : O(1)
```

---

# DP State Building

Ask yourself:

> What information do I need at every index?

Define:

```python
f(i)
```

= Maximum subarray sum **ending at index i**.

The phrase **ending at i** is extremely important.

---

# Recurrence Logic Building

At index `i`, we have only two choices.

---

## Choice 1: Start a new subarray

```python
arr[i]
```

Example:

```python
[4]
```

---

## Choice 2: Extend previous subarray

```python
arr[i] + f(i-1)
```

Example:

```python
[4,-1,2]
```

---

# Recurrence

```python
f(i) = max(
    arr[i],
    arr[i] + f(i-1)
)
```

---

# Base Case

```python
f(0) = arr[0]
```

---

# Recursive Solution

```python
def recursion(arr):
    n = len(arr)

    def f(i):
        if i == 0:
            return arr[0]

        return max(
            arr[i],
            arr[i] + f(i-1)
        )

    ans = float('-inf')

    for i in range(n):
        ans = max(ans, f(i))

    return ans
```

---

# Complexity

```text
Time  : O(N²)
Space : O(N)
```

---

# Memoization

```python
def memoization(arr):
    n = len(arr)
    memo = {}

    def f(i):
        if i == 0:
            return arr[0]

        if i in memo:
            return memo[i]

        memo[i] = max(
            arr[i],
            arr[i] + f(i-1)
        )

        return memo[i]

    ans = float('-inf')

    for i in range(n):
        ans = max(ans, f(i))

    return ans
```

---

# Complexity

```text
Time  : O(N)
Space : O(N)
```

---

# Tabulation

## DP Table

```python
dp[i]
```

= Maximum subarray sum ending at `i`.

---

# Base Case

```python
dp[0] = arr[0]
```

---

# Transition

```python
dp[i] = max(
    arr[i],
    arr[i] + dp[i-1]
)
```

---

# Code

```python
def tabulation(arr):
    n = len(arr)

    dp = [0] * n
    dp[0] = arr[0]

    ans = arr[0]

    for i in range(1, n):
        dp[i] = max(
            arr[i],
            arr[i] + dp[i-1]
        )

        ans = max(ans, dp[i])

    return ans
```

---

# Space Optimization (Actual Kadane)

Observe:

```python
dp[i]
```

depends only on:

```python
dp[i-1]
```

Therefore, we only need one variable.

---

# Code

```python
def kadane(arr):
    cur = arr[0]
    ans = arr[0]

    for i in range(1, len(arr)):
        cur = max(
            arr[i],
            arr[i] + cur
        )

        ans = max(ans, cur)

    return ans
```

---

# Complexity

```text
Time  : O(N)
Space : O(1)
```

---

# Dry Run

```python
arr = [4,-1,2,1]
```

| i | arr[i] | cur | ans |
|---|---------|-----|-----|
|0|4|4|4|
|1|-1|3|4|
|2|2|5|5|
|3|1|6|6|

Answer = 6

---

---

# Part 2: Maximum Subarray Sum with At Most One Deletion

---

# Problem Statement

Given an array `arr[]`, find the maximum sum of a non-empty subarray.

You may delete **at most one element**.

The subarray after deletion must still be **non-empty**.

---

# Example

```python
arr = [1,-2,0,3]
```

Delete:

```python
-2
```

Subarray becomes:

```python
[1,0,3]
```

Answer:

```python
4
```

---

# Main Observation

Normal Kadane state:

```python
f(i)
```

New condition:

```python
one deletion allowed
```

So we add another state.

---

# State Definition

```python
f(i, deleted)
```

where

```python
deleted = 0
```

means:

No deletion used.

```python
deleted = 1
```

means:

One deletion already used.

---

# State Meaning

---

## State 1

```python
f(i,0)
```

Maximum subarray sum ending at `i`
without using deletion.

---

## State 2

```python
f(i,1)
```

Maximum subarray sum ending at `i`
after using one deletion.

---

# Recurrence for f(i,0)

Exactly Kadane.

```python
f(i,0)=max(
    arr[i],
    arr[i]+f(i-1,0)
)
```

---

# Recurrence for f(i,1)

This is the important part.

There are only two possibilities.

---

# Case 1

Deletion happened earlier.

So we simply include current element.

```python
arr[i]+f(i-1,1)
```

---

# Case 2

Delete current element.

Then the subarray effectively ends at:

```python
i-1
```

And till `i-1`, we haven't used deletion.

So:

```python
f(i-1,0)
```

---

# Final Recurrence

```python
f(i,1)=max(
    arr[i]+f(i-1,1),
    f(i-1,0)
)
```

---

# Base Cases

```python
f(0,0)=arr[0]
```

---

```python
f(0,1)=-inf
```

Why?

Deleting the only element creates an empty subarray.

Not allowed.

---

# Recursive Solution

```python
def recursion(arr):
    n = len(arr)

    def f(i, deleted):

        if i == 0:
            if deleted == 0:
                return arr[0]
            return float('-inf')

        if deleted == 0:
            return max(
                arr[i],
                arr[i] + f(i-1,0)
            )

        return max(
            arr[i] + f(i-1,1),
            f(i-1,0)
        )

    ans = float('-inf')

    for i in range(n):
        ans = max(
            ans,
            f(i,0),
            f(i,1)
        )

    return ans
```

---

# Memoization

```python
def memoization(arr):
    n = len(arr)
    memo = {}

    def f(i, deleted):

        if i == 0:
            if deleted == 0:
                return arr[0]
            return float('-inf')

        if (i, deleted) in memo:
            return memo[(i, deleted)]

        if deleted == 0:
            ans = max(
                arr[i],
                arr[i] + f(i-1,0)
            )
        else:
            ans = max(
                arr[i] + f(i-1,1),
                f(i-1,0)
            )

        memo[(i, deleted)] = ans
        return ans

    ans = float('-inf')

    for i in range(n):
        ans = max(
            ans,
            f(i,0),
            f(i,1)
        )

    return ans
```

---

# Tabulation

---

# DP Table

```python
dp[i][0]
```

Maximum subarray sum ending at `i`
without deletion.

---

```python
dp[i][1]
```

Maximum subarray sum ending at `i`
after using one deletion.

---

# Table Size

```python
dp = [[0]*2 for _ in range(n)]
```

---

# Base Cases

```python
dp[0][0]=arr[0]
dp[0][1]=float('-inf')
```

---

# Transition

```python
dp[i][0]=max(
    arr[i],
    arr[i]+dp[i-1][0]
)
```

---

```python
dp[i][1]=max(
    arr[i]+dp[i-1][1],
    dp[i-1][0]
)
```

---

# Iteration Order

Everything depends on:

```python
i-1
```

Therefore:

```python
for i in range(1,n):
```

---

# Tabulation Code

```python
def maximumSum(arr):
    n = len(arr)

    dp = [[0]*2 for _ in range(n)

    dp[0][0] = arr[0]
    dp[0][1] = float('-inf')

    ans = arr[0]

    for i in range(1,n):

        dp[i][0] = max(
            arr[i],
            arr[i]+dp[i-1][0]
        )

        dp[i][1] = max(
            arr[i]+dp[i-1][1],
            dp[i-1][0]
        )

        ans = max(
            ans,
            dp[i][0],
            dp[i][1]
        )

    return ans
```

---

# Dry Run

```python
arr=[1,-2,0,3]
```

| i | dp[i][0] | dp[i][1] |
|---|-----------|-----------|
|0|1|-∞|
|1|-1|1|
|2|0|1|
|3|3|4|

Answer:

```python
4
```

---

# Space Optimization

Observe:

```python
dp[i][0]
```

depends only on:

```python
dp[i-1][0]
```

---

```python
dp[i][1]
```

depends only on:

```python
dp[i-1][0]
dp[i-1][1]
```

Only previous row is needed.

---

# Variables

```python
noDel
```

represents:

```python
dp[i-1][0]
```

---

```python
oneDel
```

represents:

```python
dp[i-1][1]
```

---

# Why

```python
oneDel = -inf
```

and not

```python
arr[0]
```

Because:

```python
dp[0][1]
```

means:

We already used one deletion.

Deleting the only element leaves an empty subarray.

Impossible state.

Therefore:

```python
oneDel = -inf
```

---

# Space Optimized Code

```python
def maximumSum(arr):

    noDel = arr[0]
    oneDel = float('-inf')

    ans = arr[0]

    for i in range(1, len(arr)):

        newNoDel = max(
            arr[i],
            arr[i] + noDel
        )

        newOneDel = max(
            arr[i] + oneDel,
            noDel
        )

        noDel = newNoDel
        oneDel = newOneDel

        ans = max(
            ans,
            noDel,
            oneDel
        )

    return ans
```

---

# Space Optimization Dry Run

```python
arr = [1,-2,0,3]
```

Initial:

```python
noDel = 1
oneDel = -inf
ans = 1
```

---

### i = 1

```python
newNoDel = -1
newOneDel = 1
```

---

### i = 2

```python
newNoDel = 0
newOneDel = 1
```

---

### i = 3

```python
newNoDel = 3
newOneDel = 4
```

Answer:

```python
4
```

---

# Pattern Learned Today

---

# Pattern 1

```text
Maximum Subarray
↓
Kadane DP
↓
Space Optimized DP
```

---

# Pattern 2

```text
Old DP State
+
One Extra Operation Allowed
↓
Add one Boolean State
```

Template:

```python
f(i, used)
```

where

```python
used = 0
used = 1
```

---

# When to Think of This Pattern

Questions containing:

- at most one deletion
- at most one modification
- at most one flip
- at most one transaction
- one mistake allowed
- one operation allowed

---

# General Template

```python
dp[i][0]
```

operation not used.

```python
dp[i][1]
```

operation already used.

---

# Similar Problems

1. Maximum Subarray Sum with One Deletion
2. Best Time to Buy and Sell Stock III
3. Best Time to Buy and Sell Stock IV
4. Longest Subarray of 1's After Deleting One Element
5. Max Consecutive Ones II
6. Flip One Zero to Maximize Consecutive Ones
7. Maximum Sum Circular Subarray
8. Edit Distance Variants
9. Buy and Sell Stock with Cooldown
10. Buy and Sell Stock with Transaction Fee

---

# Interview Tricks

### Trick 1

If you see:

```text
at most one operation
```

Immediately think:

```text
Old DP state + Boolean State
```

---

### Trick 2

If recurrence depends only on:

```text
i-1
```

Immediately think:

```text
Space Optimization Possible
```

---

### Trick 3

Impossible states:

For maximization DP:

```python
float('-inf')
```

For minimization DP:

```python
float('inf')
```

---

# Biggest Lesson Today

```text
Kadane is NOT Sliding Window.

Kadane is:
Recursion
↓
Memoization
↓
Tabulation
↓
Space Optimized DP
```

And:

```text
One extra operation allowed
↓
Add one Boolean State.
```