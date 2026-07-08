# 🌊 Multi-Source DFS Pattern Sheet
## (Reverse Traversal / Reachability Pattern)

> **Important**
>
> Multi-Source DFS is **not** a different algorithm.
>
> It is simply:
>
> ```
> Multiple Starting Nodes
>
> +
>
> Normal DFS
> ```
>
> The only difference from normal DFS is **where DFS starts**.

---

# Table of Contents

1. What is Multi-Source DFS?
2. Why do we need it?
3. Single Source DFS
4. Multi-Source DFS
5. When to use Multi-Source DFS
6. DFS vs Multi-Source DFS
7. Multi-Source DFS Template
8. Recognition Checklist
9. Pattern Template
10. Common Interview Problems
11. Real World Examples
12. Cheat Sheet

---

# 1. What is Multi-Source DFS?

Normally

```
One Source

↓

DFS
```

Example

```
S

↓

Visit

↓

Neighbours

↓

Go Deep
```

---

Multi-Source DFS means

```
Many Sources

↓

Start DFS

from each source
```

Example

```
A

B

C
```

Instead of

```
DFS(A)
```

We do

```
DFS(A)

DFS(B)

DFS(C)
```

Skipping already visited nodes.

---

# Important

DFS itself

does NOT change.

Only

```
Starting Points
```

change.

---

# 2. Why Do We Need It?

Suppose

```
Can every cell

reach boundary?
```

Brute Force

```
Cell 1

↓

DFS

Boundary?
```

```
Cell 2

↓

DFS

Boundary?
```

```
Cell 3

↓

DFS
```

Huge repeated work.

---

Instead

Reverse Thinking

```
Boundary

↓

Find every reachable cell.
```

Boundary has

many starting cells.

Therefore

```
Multi-Source DFS
```

---

# 3. Single Source DFS

Queue?

No.

Uses

```
Recursion

or

Stack
```

Example

```
S . .

. . .

. . .
```

Start

```
DFS(S)
```

Explore entire component.

---

# Generic Template

```python
def dfs(r,c):

    visited[r][c]=True

    for neighbour:

        if valid:

            if not visited:

                dfs(neighbour)

dfs(start)
```

---

# 4. Multi-Source DFS

Suppose

```
Boundary

O O O

↓

DFS

↓

Safe Cells
```

Instead of

```
One DFS
```

Run

```
DFS

from every boundary O
```

Already visited cells

are skipped.

---

# Initial Calls

```
DFS(Source1)

DFS(Source2)

DFS(Source3)

...

DFS(SourceN)
```

---

# DFS Itself

Does NOT change.

---

# 5. When to Use Multi-Source DFS

Whenever the problem asks

```
Can Reach?

Reach Boundary?

Reach Ocean?

Escape?

Connected to Boundary?

Safe?

Reach Destination?
```

Think

```
Reachability
```

Not

```
Shortest Distance
```

---

Usually

Destination

is

```
Boundary

Ocean

Exit

Border

Safe Zone
```

---

# Recognition Keywords

```
Reach

Connected

Escape

Boundary

Border

Ocean

Flow

Eventually Reach

Can Reach

Safe

Connected Component
```

---

# Reverse Thinking

Instead of

```
Cell

↓

Destination?
```

Think

```
Destination

↓

Find every cell
that can reach me.
```

---

# 6. DFS vs Multi-Source DFS

| Feature | DFS | Multi-Source DFS |
|----------|-----|------------------|
| Starting Node | One | Many |
| DFS Logic | Same | Same |
| Recursion | Same | Same |
| Stack | Same | Same |
| Reachability | Yes | Yes |
| Shortest Distance | No | No |
| Queue | No | No |

---

# 7. Generic Multi-Source DFS Template

```python
visited=[[False]*m for _ in range(n)]

dirs=[(0,1),(0,-1),(1,0),(-1,0)]

def dfs(r,c):

    visited[r][c]=True

    for dr,dc in dirs:

        nr=r+dr
        nc=c+dc

        if 0<=nr<n and 0<=nc<m:

            if visited[nr][nc]:
                continue

            if valid(neighbour):

                dfs(nr,nc)

# Start DFS from ALL sources

for source in all_sources:

    if not visited[source]:

        dfs(source)
```

---

# 8. Recognition Checklist

Ask yourself

```
Am I running

DFS

for every cell?
```

↓

YES

↓

```
Are all cells

trying to reach

the same destination?
```

↓

YES

↓

```
Can I reverse

the search?
```

↓

YES

↓

```
Start DFS

from destination.
```

---

# 9. Universal Pattern Template

```
Problem

↓

Can every node

reach X?

↓

Brute Force

↓

DFS from every node

↓

Repeated Work

↓

Reverse Thinking

↓

Start DFS

from X

↓

Mark Reachable

↓

Use visited

↓

Answer
```

---

# 10. Common Interview Problems

## Reverse Boundary DFS Pattern

✅ Pacific Atlantic Water Flow

```
Ocean

↓

Find Reachable Cells
```

---

✅ Surrounded Regions

```
Boundary O

↓

Find Safe O
```

---

✅ Number of Enclaves

```
Boundary Land

↓

Find Escapable Land
```

---

✅ Number of Closed Islands

```
Boundary Land

↓

Remove Reachable

↓

Count Remaining
```

---

✅ Flood Fill

Variation

---

✅ Eventual Safe States (Graph)

Reverse Graph

Same thinking.

---

# 11. Real World Examples

## Signal Towers

```
Base Stations

↓

Signal reaches towers
```

Reverse traversal.

---

## Network Reachability

```
Gateway

↓

Reachable Devices
```

---

## Escape Problem

```
Boundary Exit

↓

Who can escape?
```

---

## Water Flow

```
Ocean

↓

Reverse Flow
```

---

## Safe Area

```
Boundary Safe Zone

↓

Connected Cells
```

---

# 12. Cheat Sheet

## Single Source DFS

```
One Source

↓

Explore Component
```

---

## Multi-Source DFS

```
Many Sources

↓

Run DFS

from each source
```

---

## Reverse Boundary DFS

```
Cell

↓

Boundary?

❌

Boundary

↓

Cells

✅
```

---

# DFS vs BFS vs Multi-Source BFS

| Pattern | Main Question | Start From | Data Structure |
|----------|---------------|------------|----------------|
| DFS | Can I reach? | One source | Recursion / Stack |
| Multi-Source DFS | Which cells can reach destination? | Multiple sources (destination boundary) | Recursion / Stack |
| BFS | Shortest distance? | One source | Queue |
| Multi-Source BFS | Nearest source / spread / minimum time? | All sources simultaneously | Queue |

---

# Memory Trick

## DFS

```
Can I Reach?
```

---

## Multi-Source DFS

```
Many Sources

↓

One Reachability Search
```

---

## Reverse Boundary DFS

```
Don't ask

Cell

↓

Boundary?

Ask

Boundary

↓

Which Cells?
```

---

# One-Line Interview Rule

> **If many nodes independently ask "Can I reach the same destination?", reverse the search and start DFS from all destination boundary/source nodes. Multi-Source DFS is simply multiple DFS starting points with the same DFS logic; only the starting nodes change, not the traversal.**