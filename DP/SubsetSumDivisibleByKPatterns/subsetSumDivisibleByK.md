# Subset Sum Divisible by K

## Problem Statement

Given an array `arr[]` of positive integers and an integer `k`, determine whether there exists a **non-empty subset** whose sum is divisible by `k`.

Return:

* `True` → if such a subset exists.
* `False` → otherwise.

---

# Examples

### Example 1

```python
arr = [3, 1, 7, 5]
k = 6
```

Subset:

```python
[1, 5]
```

Sum:

```python
1 + 5 = 6
6 % 6 = 0
```

Answer:

```python
True
```

---

### Example 2

```python
arr = [1, 2, 4]
k = 8
```

No subset sum is divisible by `8`.

Answer:

```python
False
```

---

# Step 1: Brute Force Thinking

Whenever you hear:

```text
Subset
```

Your first thought should be:

```text
Take
Not Take
```

Recursion:

```python
f(i, sum)
```

Meaning:

> Starting from index `i`, can I form a subset whose current sum is `sum` and eventually becomes divisible by `k`?

Recurrence:

```python
take = f(i+1, sum + arr[i])
notTake = f(i+1, sum)

return take or notTake
```

Complexity:

```text
Time : O(2^n)
Space: O(n)
```

---

# Main Observation

Do we really need the entire `sum`?

No.

The problem only asks:

```text
sum % k == 0
```

So:

```python
sum = 17
17 % 5 = 2
```

and

```python
sum = 2
2 % 5 = 2
```

For this problem, both states are identical.

Hence we don't need:

```python
sum
```

We only need:

```python
sum % k
```

---

# State Compression

Instead of:

```python
f(i, sum)
```

we use:

```python
f(i, rem)
```

where

```python
rem = sum % k
```

---

# Why is this useful?

Possible values of remainder are only:

```text
0,1,2,...,k-1
```

Only `k` possibilities!

This reduces the state space drastically.

---

# Building the Recurrence

Suppose:

```python
current remainder = rem
```

At index `i`, we have two choices.

---

## Choice 1: Don't Take

Sum doesn't change.

Remainder also doesn't change.

```python
notTake = f(i+1, rem)
```

---

## Choice 2: Take

New sum:

```python
sum + arr[i]
```

New remainder:

```python
(sum + arr[i]) % k
```

Since:

```python
sum % k = rem
```

we can write:

```python
newRem = (rem + arr[i]) % k
```

Therefore:

```python
take = f(i+1, newRem)
```

---

# Final Recurrence

```python
f(i, rem):

    take = f(i+1, (rem + arr[i]) % k)

    notTake = f(i+1, rem)

    return take or notTake
```

---

# Handling Non-Empty Subset

The problem specifically says:

```text
Non-empty subset
```

If we start with:

```python
f(0,0)
```

then the empty subset also has remainder `0`.

We must avoid accepting it.

---

# Solution

Add one more state:

```python
taken
```

Meaning:

```text
taken = 0 → no element selected yet
taken = 1 → at least one element selected
```

State becomes:

```python
f(i, rem, taken)
```

---

# Base Case

```python
if i == n:
    return rem == 0 and taken
```

We only return `True` if:

1. remainder is `0`
2. subset is non-empty.

---

# Final Recurrence

```python
take = f(
    i+1,
    (rem + arr[i]) % k,
    1
)

notTake = f(
    i+1,
    rem,
    taken
)

return take or notTake
```

---

# Memoization

## DP State

```python
dp[i][rem][taken]
```

Meaning:

> Starting from index `i`, with current remainder `rem`, and whether we have already selected an element, can we form a valid subset?

---

## Dimensions

### Index

```text
0 → n
```

### Remainder

```text
0 → k-1
```

### Taken

```text
0 or 1
```

Therefore:

```text
DP size = (n+1) × k × 2
```

---

# Memoization Code

```python
dp = [[[-1]*2 for _ in range(k)] for _ in range(n+1)]

def f(i, rem, taken):

    if i == n:
        return rem == 0 and taken

    if dp[i][rem][taken] != -1:
        return dp[i][rem][taken]

    take = f(
        i+1,
        (rem + arr[i]) % k,
        1
    )

    notTake = f(
        i+1,
        rem,
        taken
    )

    dp[i][rem][taken] = take or notTake
    return dp[i][rem][taken]
```

Answer:

```python
f(0,0,0)
```

---

# Tabulation

## DP Table

```python
dp[i][rem][taken]
```

---

# Base Case

```python
for rem in range(k):
    dp[n][rem][0] = False
    dp[n][rem][1] = (rem == 0)
```

---

# Transition

```python
notTake = dp[i+1][rem][taken]

newRem = (rem + arr[i]) % k
take = dp[i+1][newRem][1]

dp[i][rem][taken] = take or notTake
```

---

# Tabulation Code

```python
def subsetDivisible(arr, k):
    n = len(arr)

    dp = [[[False]*2 for _ in range(k)]
          for _ in range(n+1)]

    for rem in range(k):
        dp[n][rem][0] = False
        dp[n][rem][1] = (rem == 0)

    for i in range(n-1, -1, -1):
        for rem in range(k):
            for taken in range(2):

                notTake = dp[i+1][rem][taken]

                newRem = (rem + arr[i]) % k
                take = dp[i+1][newRem][1]

                dp[i][rem][taken] = (
                    take or notTake
                )

    return dp[0][0][0]
```

Complexity:

```text
Time  : O(n*k)
Space : O(n*k)
```

---

# Space Optimized Idea (Best Solution)

Instead of storing all states, store only:

```text
All possible remainders that can be formed.
```

---

# Observation

Suppose:

```python
possible = {2,4}
```

This means:

```text
There exists some subset with remainder 2.
There exists some subset with remainder 4.
```

Now next number is:

```python
num = 7
k = 5
```

We have two choices.

---

## Start a New Subset

```python
7 % 5 = 2
```

Add:

```python
2
```

---

## Extend Old Subsets

From remainder `2`:

```python
(2+7)%5 = 4
```

From remainder `4`:

```python
(4+7)%5 = 1
```

---

# General Transition

For every remainder:

```python
newRem = (oldRem + num) % k
```

---

# Algorithm

For every number:

1. Start a new subset.
2. Extend all previous subsets.
3. Update possible remainders.

---

# Dry Run

```python
arr = [2,4]
k = 3
```

Initially:

```python
possible = {}
```

---

### Process 2

```python
new = {}

2 % 3 = 2

possible = {2}
```

---

### Process 4

Start new subset:

```python
4 % 3 = 1
```

```python
new = {2,1}
```

Extend old remainder:

```python
(2+4)%3 = 0
```

```python
new = {2,1,0}
```

Since:

```python
0 in possible
```

Answer:

```python
True
```

Subset:

```python
[2,4]
```

---

# Space Optimized Code

```python
def subsetDivisible(arr, k):

    possible = set()

    for num in arr:

        new = possible.copy()

        # subset containing only num
        new.add(num % k)

        # append num to old subsets
        for rem in possible:
            new.add((rem + num) % k)

        possible = new

        if 0 in possible:
            return True

    return False
```

---

# Complexity

```text
Time  : O(n*k)
Space : O(k)
```

Because there can be at most `k` remainders.

---

# Pigeonhole Principle Optimization

If:

```python
n > k
```

Answer is always:

```python
True
```

Reason:

There are only:

```text
k possible remainders
```

but we have more than `k` prefix sums.

Hence:

1. Some prefix remainder is `0`, OR
2. Two prefix sums have same remainder.

In both cases, some subset/subarray sum is divisible by `k`.

---

# Final Optimized Solution

```python
def subsetDivisible(arr, k):

    n = len(arr)

    if n > k:
        return True

    possible = set()

    for num in arr:

        new = possible.copy()

        new.add(num % k)

        for rem in possible:
            new.add((rem + num) % k)

        possible = new

        if 0 in possible:
            return True

    return False
```

---

# Pattern Learned

Whenever you see:

```text
Subset
+
Divisible by k
```

Immediately think:

```text
Take / Not Take
↓
State = (index, sum)
↓
Can sum be replaced by sum % k ?
↓
Remainder has only k states
↓
Modulo DP
```

---

# Real World DP Pattern

```text
Actual value is huge
↓
Question only cares about remainder/property
↓
Compress state
↓
Store only important information
```

This is called:

```text
Modulo State Compression
```

---

# Similar Problems

### 1. Continuous Subarray Sum

(Leetcode 523)

### 2. Subarrays Divisible by K

(Leetcode 974)

### 3. Count of subsets whose sum is divisible by K

### 4. Partition array into subsets with equal sum

### 5. Target Sum

(Leetcode 494)

### 6. Partition to K Equal Sum Subsets

(Leetcode 698)

### 7. Closest Subsequence Sum

(Leetcode 1755)

### 8. Count subsets with given sum

### 9. Partition Equal Subset Sum

(Leetcode 416)

### 10. Perfect Sum Problem

---

# Identification Template

Whenever the question contains:

```text
sum divisible by k
multiple of k
modulo
remainder
```

Ask yourself:

```text
Do I really need the actual sum,
or only sum % k ?
```

If the answer is:

```text
Only sum % k
```

then:

```text
Modulo DP / State Compression
```

should immediately come to your mind.
