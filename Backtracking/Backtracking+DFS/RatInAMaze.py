# Rat in a Maze

maze = [
    [1,0,0,0],
    [1,1,0,1],
    [1,1,0,0],
    [0,1,1,1]
]

def ratInMaze(maze):
    n=len(maze)
    vis=[[False]*n for _ in range(n)]

    res=[]
    def dfs(r,c,path):
        if r<0 or r>=n or c<0 or c>=n or maze[r][c]==0 or vis[r][c]:
            return 
        
        if r==n-1 and c==n-1:
            res.append(path)
            return 
        
        vis[r][c]=True 

        dfs(r+1,c,path+"D")
        dfs(r,c-1,path+"L")
        dfs(r,c+1,path+"R")
        dfs(r-1,c,path+"U")

        vis[r][c]=False

    dfs(0,0,"")
    return res

print(ratInMaze(maze))