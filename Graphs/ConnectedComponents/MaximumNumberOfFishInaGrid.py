# Maximum Number of Fish in a grid LC 2658

grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]

def findMaxFish(grid):
    if not grid:
        return 0

    n, m = len(grid), len(grid[0])
    vis = [[False] * m for _ in range(n)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = 0

    def dfs(r, c):
        count=grid[r][c]
        vis[r][c] = True
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if 0<=nr<n and 0<=nc<m and grid[nr][nc] and not vis[nr][nc]:
                count+=dfs(nr,nc)
        return count
    for i in range(n):
        for j in range(m):
            if grid[i][j]!=0 and not vis[i][j]:
                res=max(res,dfs(i,j))
    return res

print(findMaxFish(grid))