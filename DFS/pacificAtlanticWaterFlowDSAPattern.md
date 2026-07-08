# 🌊 Pacific Atlantic Water Flow / Two Stations Matrix Problem
# PART 4 — Permanent DSA Pattern Sheet (Interview Revision)

---

# 📌 Pattern Name

```
Reverse Flow + Multi-Source DFS/BFS
```

Also Known As

```
Reverse Graph Traversal

Multi-Source DFS

Reverse Reachability

Ocean Flow Pattern
```

---

# The Core Idea

Instead of asking

```
Can every node
reach Destination?
```

Ask

```
Can Destination
discover every node
that can reach it?
```

This single question converts

```
O((n*m)^2)

↓

O(n*m)
```

---

# The Pattern

Suppose interview asks

```
Find all cells
that can reach X.
```

Most beginners think

```
Every Cell

↓

DFS

↓

Reach X?
```

Wrong direction.

Instead think

```
X

↓

Reverse DFS

↓

Find every reachable cell.
```

---

# Recognition Pattern

Whenever you read

```
Can reach...
```

Immediately ask yourself

```
Can I reverse the search?
```

---

# Recognition Keywords

These words should trigger this pattern.

```
Reach

Flow

Spread

Propagate

Transmit

Travel

Escape

Drain

Water

Signal

Ocean

Boundary

Exit

Border

Destination

Can reach

Eventually reach

Connected to
```

---

# Recognition Checklist

While reading the problem ask

```
1.

Am I checking
whether every node
reaches one destination?

YES

↓

Go Next.
```

---

```
2.

Will DFS from every node
repeat work?

YES

↓

Go Next.
```

---

```
3.

Can I start
from the destination?

YES

↓

Go Next.
```

---

```
4.

Can I reverse
the movement rule?

YES

↓

Reverse DFS/BFS.
```

---

# Biggest Observation

Brute Force

```
Cell

↓

Destination?
```

Optimization

```
Destination

↓

Cell
```

Nothing else changes.

---

# Reverse Flow Rule

Original

```
Neighbour <= Current
```

Reverse

```
Neighbour >= Current
```

General Formula

```
Reverse

=

Reverse every edge.
```

---

# Important Interview Question

Interviewer

```
Why >= ?
```

Answer

```
Because during reverse DFS
I'm asking

"Could this neighbour
have reached me
in the original graph?"

If yes,

I move there.
```

Never say

```
Because reverse flow.
```

Explain WHY.

---

# Interview Thinking Framework

Always think in this order.

---

## Step 1

Understand movement.

```
How can I move?
```

---

## Step 2

Find destination.

```
Where am I trying to reach?
```

---

## Step 3

Brute Force

```
Run DFS

from every node.
```

---

## Step 4

Observe repetition.

```
Same cells

visited

again and again.
```

---

## Step 5

Reverse the question.

Instead of

```
Can node reach destination?
```

Think

```
Can destination
find all nodes?
```

---

## Step 6

Reverse movement.

```
<=

↓

>=
```

---

## Step 7

Run Multi-Source DFS.

---

## Step 8

Collect answer.

---

# Generic Algorithm Template

```
Destination Cells

↓

Push into DFS/BFS

↓

Reverse Movement

↓

Mark Reachable

↓

Repeat for every destination

↓

Intersection

↓

Answer
```

---

# Universal Code Template

```python
visited=[[False]*m for _ in range(n)]

def dfs(r,c):

    visited[r][c]=True

    for neighbour:

        if valid:

            if visited:

                continue

            if reverse_condition:

                dfs(neighbour)
```

Then

```python
for every source:

    dfs(source)
```

Done.

---

# How to Identify Reverse Graph Problems

If interviewer asks

```
Can every node
reach one node?
```

Think

```
Reverse Graph.
```

---

If interviewer asks

```
Can every city
reach capital?
```

Think

```
Start from capital.
```

---

If interviewer asks

```
Can every room
reach exit?
```

Think

```
Start from exit.
```

---

If interviewer asks

```
Can every student
reach principal office?
```

Think

```
Start from office.
```

---

# Real World Analogies

---

## Example 1

Bus Stop

Question

```
Which houses
can reach Bus Stop?
```

Wrong

```
House1

↓

Bus Stop
```

```
House2

↓

Bus Stop
```

Correct

```
Bus Stop

↓

Walk backwards

↓

Find every house.
```

---

## Example 2

River

Question

```
Which villages
can send water
to river?
```

Wrong

```
Village

↓

River
```

Correct

```
River

↓

Move uphill

↓

Find villages.
```

---

## Example 3

Internet

Question

```
Which computers
can send packets
to server?
```

Wrong

```
Computer

↓

Server
```

Correct

```
Server

↓

Reverse connections

↓

Find computers.
```

---

# Why Multi-Source DFS?

Pacific is NOT

```
One Cell.
```

Pacific is

```
Entire Boundary.
```

Therefore

Sources

```
Top Row

+

Left Column
```

Similarly

Atlantic

```
Bottom Row

+

Right Column
```

Whenever destination has

```
Many starting points

↓

Multi-Source DFS/BFS
```

should click.

---

# Common Mistakes

## Mistake 1

Memorizing

```
>=
```

Instead derive it.

---

## Mistake 2

Thinking

```
Water reversed.
```

Wrong.

Search reversed.

---

## Mistake 3

Starting DFS

from every cell.

---

## Mistake 4

Forgetting

Visited Matrix.

---

## Mistake 5

Running DFS

without reverse condition.

---

# Similar Interview Problems

## 1. Pacific Atlantic Water Flow (LeetCode 417)

Exactly this pattern.

---

## 2. Surrounded Regions (LeetCode 130)

```
Border

↓

Reverse DFS

↓

Mark Safe Cells
```

Pattern

```
Reverse Boundary DFS
```

---

## 3. Number of Enclaves (LeetCode 1020)

```
Boundary

↓

Remove reachable land

↓

Remaining answer.
```

Same idea.

---

## 4. Walls and Gates (LeetCode 286)

```
All Gates

↓

Multi-Source BFS

↓

Fill Distances.
```

---

## 5. Rotting Oranges (LeetCode 994)

```
All Rotten

↓

Multi-Source BFS.
```

---

## 6. 01 Matrix (LeetCode 542)

```
All Zeroes

↓

Multi-Source BFS.
```

---

## 7. Escape Large Maze

Reverse thinking appears.

---

## 8. Reverse Graph Reachability

Any graph problem asking

```
Who can reach destination?
```

---

# Pattern Family

```
Grid DFS

↓

Boundary DFS

↓

Reverse DFS

↓

Multi Source DFS

↓

Reverse Graph
```

These are all closely related.

---

# Complexity Pattern

Brute Force

```
Nodes

×

DFS

=

O(V²)
```

Reverse DFS

```
One Traversal

=

O(V)
```

Grid

```
O(n*m)
```

---

# Questions to Ask Yourself During Interview

```
1.

Am I starting DFS
from every node?
```

---

```
2.

Am I repeating work?
```

---

```
3.

Can I reverse
the search?
```

---

```
4.

Can destination
be my starting point?
```

---

```
5.

Do I have
multiple destinations?

↓

Multi-Source DFS?
```

---

```
6.

What happens
to movement rule
after reversing?
```

---

# One-Line Recognition Rule

```
Node → Destination ?

↓

Think

Destination → Node
```

---

# 30-Second Revision Sheet

```
Problem

↓

Can node reach destination?

↓

Brute Force

DFS from every node

↓

Repeated work

↓

Reverse Search

↓

Start from destination

↓

Reverse movement

↓

Multi-Source DFS

↓

Visited Matrix

↓

Intersection

↓

Answer
```

---

# 10-Second Interview Cheat Sheet

```
Destination?

↓

Reverse DFS

↓

>=

↓

Multi Source

↓

Visited

↓

Intersection
```

---

# Master Formula

Whenever you see

```
Can every node
reach X?
```

Immediately think

```
Start from X

↓

Reverse DFS/BFS

↓

Mark all reachable nodes

↓

Done.
```

---

# Final Takeaway

This problem is **not about matrices**.

It is **not about water**.

It is **not about DFS**.

The real interview pattern is:

> **Whenever many nodes independently ask "Can I reach the same destination?", consider reversing the search. Start from the destination (or all destination boundary cells), traverse the graph in reverse, and mark every node that can reach it.**

Once this pattern clicks, you'll recognize it in many graph and grid problems—not just Pacific Atlantic Water Flow.