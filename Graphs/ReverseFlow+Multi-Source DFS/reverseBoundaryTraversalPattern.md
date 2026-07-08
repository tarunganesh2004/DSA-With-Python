# 🌊 Reverse Boundary Traversal Pattern
# Master Notes (Pacific Atlantic + Surrounded Regions + Number of Enclaves)

---

# Why These 3 Problems Are Studied Together

At first glance, these look like completely different problems.

| Problem | Story |
|----------|-------|
| Pacific Atlantic | Water Flow |
| Surrounded Regions | O and X |
| Number of Enclaves | Land and Water |

But internally they all ask the same question.

> **Can many cells reach the same destination?**

Whenever you see this,

don't start DFS from every cell.

Instead think

```
Can I start from the destination
and discover every cell that can reach it?
```

This is the **Reverse Boundary Traversal Pattern**.

---

# Problem 1 — Pacific Atlantic Water Flow

## Problem

Each cell has a height.

Water can flow

```
Higher

↓

Lower or Equal
```

Need to find

```
Cells

↓

Can reach Pacific

AND

Can reach Atlantic
```

---

## Brute Force

For every cell

```
DFS

↓

Can Reach Pacific?

DFS

↓

Can Reach Atlantic?
```

Time

```
O((n*m)^2)
```

---

## Optimization

Start from

```
Pacific Boundary
```

Reverse DFS

```
Neighbour >= Current
```

Mark

```
Pacific Reachable
```

Again

Start from

```
Atlantic Boundary
```

Reverse DFS.

Answer

```
Intersection
```

---

## Meaning of visited

```
visited

↓

Can Reach Ocean
```

---

# Problem 2 — Surrounded Regions

## Problem

Replace every O that is completely surrounded by X.

Keep

```
Boundary O

+

Connected O
```

---

## Brute Force

For every O

```
DFS

↓

Can Reach Boundary?
```

Time

```
O((n*m)^2)
```

---

## Optimization

Start DFS from

```
Boundary O's
```

Mark

```
Safe O
```

Finally

```
Every O

AND

Not Safe

↓

Convert to X
```

---

## Meaning of visited

```
visited

↓

Safe O
```

---

# Problem 3 — Number of Enclaves

## Problem

Count land cells

```
1
```

that cannot reach boundary.

---

## Brute Force

For every land

```
DFS

↓

Can Reach Boundary?
```

Time

```
O((n*m)^2)
```

---

## Optimization

Start DFS from

```
Boundary Land
```

Mark

```
Escapable Land
```

Finally

```
Land

AND

Not Visited

↓

Count
```

---

## Meaning of visited

```
visited

↓

Can Escape
```

---

# Common Pattern

All three problems follow exactly the same thinking.

---

## Step 1

Brute Force

```
For every cell

↓

Run DFS

↓

Can it reach destination?
```

---

## Step 2

Observe

```
Repeated DFS
```

Many searches explore the same component.

---

## Step 3

Reverse Thinking

Instead of

```
Cell

↓

Destination?
```

Ask

```
Destination

↓

Which cells
can reach me?
```

---

## Step 4

Start DFS from destination.

---

## Step 5

Mark every reachable cell.

---

## Step 6

Use visited information.

---

# Generic Algorithm

```
Identify destination

↓

Start DFS/BFS from destination

↓

Mark reachable cells

↓

Traverse entire grid

↓

Use visited information

↓

Answer
```

---

# Comparison Table

| Feature | Pacific Atlantic | Surrounded Regions | Number of Enclaves |
|---------|------------------|--------------------|--------------------|
| Brute Force Question | Can cell reach Pacific & Atlantic? | Can O reach boundary? | Can land reach boundary? |
| Destination | Pacific + Atlantic | Boundary O | Boundary Land |
| DFS Starts From | Ocean Boundaries | Boundary O's | Boundary Land |
| Reverse DFS Needed? | Yes | Yes | Yes |
| Movement Rule | `>=` (reverse flow) | Adjacent O | Adjacent Land |
| Visited Means | Can reach ocean | Safe O | Escapable Land |
| Final Step | Pacific ∩ Atlantic | Flip unsafe O to X | Count unvisited land |
| Output | Count | Modified Grid | Count |

---

# Recognition Keywords

Whenever you read words like

```
Reach

Flow

Boundary

Escape

Connected

Propagate

Eventually Reach

Can Reach

Ocean

Exit

Border
```

Immediately ask

```
Can I reverse the search?
```

---

# Recognition Checklist

```
1.

Am I checking

every cell

individually?
```

↓

```
YES
```

↓

```
2.

Is every cell

trying to reach

the same destination?
```

↓

```
YES
```

↓

```
3.

Can I start

from destination?
```

↓

```
YES
```

↓

```
Reverse DFS/BFS
```

---

# Mental Model

Never think

```
Cell

↓

Destination
```

Instead think

```
Destination

↓

Find Every Cell
```

---

# One-Line Memory Trick

```
Many Cells

↓

One Destination

↓

Reverse Search
```

---

# Pattern Template (Permanent Revision)

```
Problem asks

↓

Can every node

reach X?

↓

Brute Force

↓

DFS from every node

↓

Repeated work

↓

Reverse Thinking

↓

Start from X

↓

DFS/BFS

↓

Mark reachable

↓

Traverse grid

↓

Answer
```

---

# Similar Interview Problems

## Same Reverse Boundary DFS Pattern

- Pacific Atlantic Water Flow
- Surrounded Regions
- Number of Enclaves
- Closed Islands
- Flood Fill (variation)
- Eventual Safe States (graph version)

---

## Same Multi-Source Traversal Family

- Rotting Oranges
- 01 Matrix
- Walls and Gates
- Shortest Bridge
- As Far From Land As Possible

---

# Final Interview Takeaway

These problems are **not about water**, **O/X**, or **land**.

They all belong to the same underlying family:

> **When many cells independently ask "Can I reach the same destination?", reverse the search. Start from the destination (or destination boundary), traverse outward, mark all reachable cells, and derive the answer from the visited matrix.**