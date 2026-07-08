# Max Area of Island LC 695

grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]

def maxAreaOfIsland(grid):
    if not grid:
        return 0
    
    n,m=len(grid),len(grid[0])
    vis=[[False]*m for _ in range(n)]
    dirs=[(0,1),(0,-1),(1,0),(-1,0)]
    maxArea=0

    def dfs(r,c):
        if vis[r][c]:
            return 0
        vis[r][c]=True
        area=1
        for dr,dc in dirs:
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<m:
                if vis[nr][nc]:
                    continue 
                if grid[nr][nc]==1:
                    area+=dfs(nr,nc) 

        return area 

    
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and not vis[i][j]:
                maxArea=max(maxArea,dfs(i,j))
    return maxArea

print(maxAreaOfIsland(grid))