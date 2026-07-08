# Number of Islands LC 200

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]


def numIslands(grid):
    if not grid:
        return 0
    n,m=len(grid),len(grid[0])
    ans=0

    dirs=[(0,1),(0,-1),(1,0),(-1,0)]
    vis=[[False]*m for _ in range(n)]
    def dfs(r,c):
        vis[r][c]=True
        for dr,dc in dirs:
            nr,nc=r+dr,c+dc 
            if 0<=nr<n and 0<=nc<m:
                if vis[nr][nc]:
                    continue

                if grid[nr][nc]=="1":
                    vis[nr][nc]=True
                    dfs(nr,nc)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="1" and not vis[i][j]:
                dfs(i,j)
                ans+=1
    return ans 

print(numIslands(grid))

"""
Similar qsns 
Max Area of Island (LC 695)
Count sub islands (LC 1905)
Count islands with total Value divisible by K (LC 3619)
Maximum Number of Fish in a Grid (LC 2658)
"""