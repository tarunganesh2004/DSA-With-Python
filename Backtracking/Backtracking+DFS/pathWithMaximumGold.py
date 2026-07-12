# Path with Maximum Gold LC 1219

grid=[
    [0,6,0],
    [5,8,7],
    [0,9,0]
]

def getMaximumGold(grid):
    n=len(grid)
    m=len(grid[0])
    vis=[[False]*m for _ in range(n)]
    

    def dfs(r,c):
       
        if r<0 or r>=n or c<0 or c>=m or grid[r][c]==0 or vis[r][c]:
            return 0
        
        vis[r][c]=True 

        best =max(
            dfs(r+1,c),
            dfs(r-1,c),
            dfs(r,c+1),
            dfs(r,c-1)
        )

        vis[r][c]=False 

        # current gold+best possible future gold
        return grid[r][c]+best
        
    ans=0
    # run dfs through every possible starting point 
    for r in range(n):
        for c in range(m):
            if grid[r][c]!=0:
                ans=max(ans,dfs(r,c))

    return ans 

print(getMaximumGold(grid))