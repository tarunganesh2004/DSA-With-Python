# 🌊 Multi-Source BFS Pattern Sheet
## (One of the Most Important Graph/Grid Interview Patterns)

---

# Table of Contents

1. What is BFS?
2. Why BFS gives Shortest Distance
3. When to use BFS over DFS
4. Single Source BFS
5. Multi-Source BFS
6. How to identify Multi-Source BFS
7. BFS vs DFS
8. Single Source vs Multi-Source BFS
9. Generic BFS Template
10. Generic Multi-Source BFS Template
11. Recognition Checklist
12. Pattern Template
13. Interview Problems
14. Real World Examples
15. Cheat Sheet

---

# 1. What is BFS?

BFS stands for

```
Breadth First Search
```

Unlike DFS,

```
DFS

↓

Go Deep
```

BFS explores

```
Level by Level

↓

Layer by Layer
```

Example

```
        A
      / | \
     B  C  D
    / \
   E   F
```

BFS Order

```
A

↓

B C D

↓

E F
```

DFS

```
A

↓

B

↓

E

↓

Backtrack

↓

F

↓

C

↓

D
```

---

# 2. Why BFS Finds Shortest Distance

Suppose

```
S . . .

. . . .

. . . D
```

Each move costs

```
1
```

BFS explores

```
Distance = 0

↓

Distance = 1

↓

Distance = 2

↓

Distance = 3
```

The first time we reach

```
Destination
```

it is guaranteed to be

```
Minimum Distance
```

DFS cannot guarantee this.

---

# Visual

```
Layer 0

S

↓

Layer 1

*

↓

Layer 2

**

↓

Layer 3

***

↓

Destination
```

---

# 3. When to Use BFS Over DFS

Whenever the problem asks

```
Nearest

Minimum

Shortest

Distance

Steps

Moves

Minutes

Time

Levels

Spread

Infection

Fire

Rotting

Wave

Closest
```

Immediately think

```
BFS
```

---

# Why NOT DFS?

DFS

```
Go Deep

↓

May find a very long path first

↓

Not guaranteed shortest
```

BFS

```
Explore all shorter paths first

↓

Guaranteed shortest
```

---

# BFS Recognition Keywords

```
Nearest

Closest

Minimum Distance

Shortest Path

Minimum Steps

Minimum Moves

Minutes

Hours

Time Taken

Spread

Rot

Wave

Flood

Infection
```

---

# 4. Single Source BFS

Meaning

```
One Starting Point
```

Example

```
S . .

. . .

. . D
```

Queue initially

```
[S]
```

BFS expands

```
S

↓

Neighbours

↓

Next Layer

↓

Next Layer
```

---

# Generic Single Source BFS Template

```python
from collections import deque

q = deque()

visited = [[False]*m for _ in range(n)]

q.append((sr, sc))
visited[sr][sc] = True

while q:

    r, c = q.popleft()

    for dr, dc in dirs:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < n and 0 <= nc < m:

            if not visited[nr][nc]:

                visited[nr][nc] = True

                q.append((nr, nc))
```

---

# Time Complexity

```
O(V + E)

Grid

↓

O(n*m)
```

---

# 5. Multi-Source BFS

Suppose

```
🔥 . . .

. . . .

. . . 🔥

. 🔥 . .
```

Question

```
Distance

to nearest fire
```

Brute Force

```
Fire 1

↓

Entire BFS

Fire 2

↓

Entire BFS

Fire 3

↓

Entire BFS
```

Huge repeated work.

---

Instead

Start

```
ALL

fires

together.
```

Queue initially

```
[(0,0),

(2,3),

(3,1)]
```

One BFS.

---

# Why It Works

Imagine

```
Fire spreads

every minute.
```

Minute 0

```
🔥
```

Minute 1

```
Adjacent
```

Minute 2

```
Next Layer
```

Exactly

what BFS naturally does.

---

# 6. Multi-Source BFS Recognition

Ask

```
Are multiple sources

spreading

simultaneously?
```

If

```
YES
```

Think

```
Multi-Source BFS
```

---

# Common Keywords

```
Nearest Source

Nearest Zero

Nearest Gate

Rotting

Infection

Fire

Spread

Wave

Simultaneously

Minimum Distance

Closest
```

---

# Multi-Source BFS Idea

Instead of

```
One Source

↓

BFS
```

Think

```
All Sources

↓

ONE BFS
```

---

# Biggest Difference

Single Source

```
Queue

↓

One Cell
```

Multi Source

```
Queue

↓

ALL Starting Cells
```

Nothing else changes.

---

# 7. BFS vs DFS

| Feature | DFS | BFS |
|----------|-----|-----|
| Data Structure | Stack / Recursion | Queue |
| Traversal | Depth First | Level Order |
| Shortest Distance | ❌ | ✅ |
| Reachability | ✅ | ✅ |
| Connected Components | ✅ | ✅ |
| Distance Problems | ❌ | ✅ |
| Flood Fill | ✅ | ✅ |
| Multi Source | Rare | Very Common |

---

# When DFS is Better

```
Can Reach?

Connected?

Island?

Boundary?

Cycle?

Component?

Backtracking?
```

---

# When BFS is Better

```
Nearest?

Shortest?

Minimum?

Distance?

Time?

Minutes?

Spread?
```

---

# 8. Single Source vs Multi-Source BFS

| Feature | Single Source | Multi Source |
|----------|---------------|--------------|
| Starting Nodes | One | Many |
| Queue Initially | One Cell | All Sources |
| Traversal | Same | Same |
| Complexity | O(V+E) | O(V+E) |
| Typical Problems | Shortest Path | Spread / Nearest Source |

---

# 9. Generic BFS Template

```python
from collections import deque

q = deque()

q.append(start)

visited[start] = True

while q:

    node = q.popleft()

    for neighbour in neighbours:

        if not visited[neighbour]:

            visited[neighbour] = True

            q.append(neighbour)
```

---

# 10. Generic Multi-Source BFS Template

```python
from collections import deque

q = deque()

visited = [[False]*m for _ in range(n)]

# Push ALL sources

for i in range(n):
    for j in range(m):

        if grid[i][j] is SOURCE:

            q.append((i, j))

            visited[i][j] = True

while q:

    r, c = q.popleft()

    for dr, dc in dirs:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < n and 0 <= nc < m:

            if not visited[nr][nc]:

                visited[nr][nc] = True

                q.append((nr, nc))
```

---

# Multi-Source BFS with Distance

```python
from collections import deque

q = deque()

dist = [[-1]*m for _ in range(n)]

for every source:

    q.append(source)

    dist[source] = 0

while q:

    r, c = q.popleft()

    for neighbour:

        if dist[neighbour] == -1:

            dist[neighbour] = dist[r][c] + 1

            q.append(neighbour)
```

---

# 11. Recognition Checklist

Ask yourself

```
Is this asking

Shortest Distance?
```

↓

YES

↓

```
Does movement cost

1 step?
```

↓

YES

↓

```
Are there

multiple starting points?
```

↓

YES

↓

```
Multi-Source BFS
```

Otherwise

```
Single Source BFS
```

---

# 12. Universal Pattern Template

```
Problem

↓

Need Minimum Distance?

↓

YES

↓

BFS

↓

Multiple Sources?

↓

YES

↓

Put ALL sources into Queue

↓

Level Order Expansion

↓

Answer
```

---

# 13. Similar Interview Problems

## Single Source BFS

- Binary Maze
- Shortest Path in Binary Matrix
- Word Ladder
- Knight Minimum Moves

---

## Multi-Source BFS

- 01 Matrix ⭐⭐⭐⭐⭐
- Rotting Oranges ⭐⭐⭐⭐⭐
- Walls and Gates ⭐⭐⭐⭐⭐
- As Far From Land As Possible ⭐⭐⭐⭐
- Shortest Bridge ⭐⭐⭐⭐

---

# 14. Real World Examples

## Virus Spread

```
Initially

5 infected people

↓

Virus spreads

simultaneously
```

Multi-Source BFS

---

## Fire Spread

```
Multiple fire sources

↓

Spread together
```

Multi-Source BFS

---

## Multiple Hospitals

```
Nearest Hospital

↓

Distance
```

Multi-Source BFS

---

## WiFi Routers

```
Multiple Routers

↓

Signal spreads
```

Multi-Source BFS

---

## Flood

```
Water enters

from multiple locations

↓

Spreads together
```

Multi-Source BFS

---

# 15. Ultimate Cheat Sheet

## DFS

```
Reachability

Connected Components

Boundary Problems

Flood Fill

Cycle Detection
```

---

## BFS

```
Shortest Distance

Minimum Steps

Nearest

Time

Levels
```

---

## Multi-Source BFS

```
Many Sources

↓

One BFS

↓

Nearest Source

↓

Spread

↓

Minimum Distance
```

---

# Memory Trick

## DFS

```
Can I Reach?
```

---

## BFS

```
How Fast Can I Reach?
```

---

## Multi-Source BFS

```
Everyone Starts Together

↓

Spread Level by Level
```

---

# One-Line Interview Rule

> **If the problem asks "Can I reach?" → think DFS.  
> If it asks "How many steps/minutes/shortest distance?" → think BFS.  
> If there are multiple starting points spreading simultaneously, initialize the queue with all of them and use Multi-Source BFS.**