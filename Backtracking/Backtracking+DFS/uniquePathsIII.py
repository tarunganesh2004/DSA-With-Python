# Unique Paths III LC 980(Hard)

grid=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]

def uniquePathsIII(grid):
    n=len(grid)
    m=len(grid[0])

    vis=[[False]*m for _ in range(n)]

    remaining=0
    start_r,start_c=0,0
    # find start cell and all walkable cells
    for r in range(n):
        for c in range(m):
            if grid[r][c]!=-1:
                remaining+=1
            
            if grid[r][c]==1:
                start_r=r
                start_c=c

    def dfs(r,c,remaining):

        if r<0 or r>=n or c<0 or c>=m or vis[r][c] or grid[r][c]==-1:
            return 0
        
        if grid[r][c]==2:
            return 1 if remaining==1 else 0 
        
        vis[r][c]=True 
        remaining-=1

        paths=(dfs(r+1,c,remaining)+dfs(r-1,c,remaining)+dfs(r,c+1,remaining)+dfs(r,c-1,remaining))
        vis[r][c]=False

        return paths 
    
    return dfs(start_r,start_c,remaining)

print(uniquePathsIII(grid))

