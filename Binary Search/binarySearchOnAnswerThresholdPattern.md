# 📘 DSA Pattern Sheet: Binary Search on Answer (Threshold / Leveling Pattern)

---

# Pattern Name

> **Binary Search on Answer (Threshold / Leveling Pattern)**

Also combines:

- Greedy
- Arithmetic Progression (Range Sum)
- Leveling Technique

---

# Core Idea

Most beginners think:

> **"Which operation should I perform next?"**

Experts think:

> **"What is the final threshold (level) after all operations?"**

Instead of simulating every operation, search for the **final answer directly**.

---

# Thinking Evolution

```
Brute Force

↓

Simulate every operation

↓

Too Slow

↓

Can multiple operations be grouped together?

↓

Represent grouped operations by a Threshold / Level

↓

Can we check any threshold in O(n)?

↓

YES

↓

Is the check monotonic?

↓

YES

↓

Binary Search on Answer

↓

Compute final result mathematically
```

---

# Recognition Checklist

Whenever you see

✅ Repeated operations

✅ Large constraints (10⁵ or more)

✅ Simulation is expensive

✅ Values increase/decrease gradually

✅ Need Maximum/Minimum answer

Ask yourself

```
Can I stop simulating
and instead search for a final level?
```

If YES

↓

Write a **check(mid)** function.

If

```
check(mid)
```

is monotonic

↓

Binary Search on Answer.

---

# What is a Threshold?

A threshold is simply a **common stopping point**.

Example

```
10
7
5
```

Suppose threshold

```
6
```

Everything above 6 becomes

```
6
```

Result

```
6
6
5
```

We no longer care about individual operations.

We only care about

> **"How much work is needed to reach this level?"**

---

# How to Build the Logic

## Step 1

Start with brute force.

Ask

```
What am I repeating?
```

Example

```
Sell one ticket.

Sell one ticket.

Sell one ticket.
```

---

## Step 2

Ask

```
Can many operations be done together?
```

Example

Instead of

```
10

9

8

7
```

Calculate

```
10+9+8+7
```

using Arithmetic Progression.

---

## Step 3

Ask

```
Where should I stop?
```

Instead of thinking

```
Next ticket
```

Think

```
Final Level
```

---

## Step 4

Create a Check Function

Example

```
Threshold = mid
```

Question

```
If every value above mid is reduced to mid,

How many operations are needed?
```

Usually

```
O(n)
```

---

## Step 5

Observe the Behaviour

As threshold increases

```
Operations decrease
```

or

As threshold decreases

```
Operations increase
```

This creates

```
Monotonic Behaviour
```

which is the key requirement for Binary Search.

---

# Monotonic Property

Example

```
10
7
5
```

| Threshold | Operations |
|-----------|-----------:|
|8|2|
|7|3|
|6|5|
|5|7|

Observe

```
Threshold ↑

Operations ↓
```

Always.

Whenever this happens

↓

Binary Search.

---

# General Binary Search Template

```python
low = minimum_answer
high = maximum_answer

while low <= high:

    mid = (low + high) // 2

    if check(mid):

        answer = mid

        # move according to problem
        low = mid + 1

    else:

        high = mid - 1
```

Entire trick lies inside

```
check(mid)
```

---

# Generic Check Function

Most Binary Search on Answer problems become

```python
def check(mid):

    value = 0

    for x in arr:

        # Compute work for this threshold

    return value >= required
```

Sometimes

```
>=
```

Sometimes

```
<=
```

depends on the problem.

---

# Arithmetic Progression Trick

Whenever simulation looks like

```
10

9

8

7
```

Instead use

```
First = 10

Last = 7

Count = 4

Sum = (First + Last) × Count // 2
```

Converts

```
O(k)

↓

O(1)
```

---

# Common Patterns That Use This Idea

## 1. Binary Search on Answer

Examples

- Koko Eating Bananas
- Capacity To Ship Packages
- Allocate Minimum Pages
- Painter Partition
- Aggressive Cows
- Maximum Candies Allocation

---

## 2. Threshold / Leveling

Examples

```
Reduce heights

Fill water

Cut wood

Allocate capacity

Sell decreasing values

Equalize values
```

---

## 3. Greedy

Local optimal choice

```
Always choose best current option.
```

Example

```
Sell highest ticket.
```

---

## 4. Arithmetic Progression

Whenever values are

```
10

9

8

7
```

Don't loop.

Use formula.

---

# Common Interview Flow

Interviewer gives

```
Brute Force
```

↓

Improve

```
Heap
```

↓

Still slow

↓

Observe repeated pattern

↓

Batch operations

↓

Threshold

↓

Binary Search

↓

Math Formula

---

# Real World Examples

## Water Tanks

```
10L

7L

5L
```

Lower every tank to

```
6L
```

instead of removing water litre by litre.

---

## Salary Reduction

Employees

```
100

90

70
```

Reduce everyone above

```
80
```

No need to reduce salary one dollar at a time.

---

## Mountain Leveling

```
10

8

6
```

Bulldoze everything above height

```
6
```

instead of removing one rock at a time.

---

## Ticket Selling Problem

Instead of

```
Sell

10

9

8

7
```

Think

```
Reduce seller

10

↓

6
```

Then compute earnings directly.

---

# Pattern Recognition Sheet

Whenever you see

```
Repeated simulation

↓

Large constraints

↓

Need Max/Min answer

↓

Can imagine a common level

↓

Can write check(mid)

↓

Check is monotonic

↓

Binary Search on Answer
```

---

# Questions to Ask Yourself

1. What is being repeated?

2. Can I batch these operations?

3. Can I replace operations by a threshold?

4. Can I check any threshold in O(n)?

5. Does the answer change monotonically?

6. Can Binary Search find this threshold?

7. Can the remaining work be computed using mathematics instead of simulation?

---

# Golden Rules

✅ Simulating one operation at a time is often too slow.

✅ Think in **Levels**, not individual operations.

✅ Threshold problems usually become Binary Search.

✅ Consecutive values usually indicate Arithmetic Progression.

✅ Binary Search on Answer is about searching a **value**, not an **index**.

---

# Master Template

```
Repeated Simulation

↓

Identify expensive operation

↓

Can operations be grouped?

↓

Represent group using Threshold

↓

Build check(mid)

↓

Check is Monotonic

↓

Binary Search

↓

Mathematical Computation

↓

Optimal Solution
```

---

# One-Line Memory Trick

> **"When simulation is too slow, stop thinking about the next operation—start thinking about the final threshold."**