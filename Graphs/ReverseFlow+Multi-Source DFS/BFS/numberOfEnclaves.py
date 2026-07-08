# Number of enclaves LC 1020

grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

# brute force is do dfs on every land cell and find whether this reaches boundary or not 


# optimized is same pattern (pacific atlantic)
# instead of asking can this land -> reach boundary
# ask boundary land cell -> which land can reach me 
# so start dfs from all boundary land cells 
# so every land we visit is escapable, every land we dont visit is trapped(enclaved)

def numEnclaves(grid):
    n=len(grid)
    m=len(grid[0])

    vis=[[False]*m for _ in range(n)]

    dirs=[(0,1),(0,-1),(1,0),(-1,0)]
    ans=0

    def dfs(r,c):
        vis[r][c]=True 

        for dr,dc in dirs:
            nr=r+dr
            nc=c+dc 

            if 0<=nr<n and 0<=nc<m:
                if vis[nr][nc]:
                    continue 

                if grid[nr][nc]!=0 :
                    dfs(nr,nc)
    # now same as previous problems(pacific atlantic and surrounded regions ),
    #  check everyboundary (top row,bottom, left col,right col)
    # top row 
    for j in range(m):
        if grid[0][j]==1 and not vis[0][j]:
            dfs(0,j)
    
    # bottom row 
    for j in range(m):
        if grid[n-1][j]==1 and not vis[n-1][j]:
            dfs(n-1,j)

    # left column 
    for i in range(n):
        if grid[i][0]==1 and not vis[i][0]:
            dfs(i,0)
    
    # right column 
    for i in range(n):
        if grid[i][m-1]==1 and not vis[i][m-1]:
            dfs(i,m-1)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and not vis[i][j]:
                ans+=1
    return ans 

print(numEnclaves(grid))