# Surrounded Regions LC 130

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]

# qsn is is can the O reach any boundary O by moving through only O's 
# if yes keep 0 else convert to x 

# this pattern same as pacific atlantic waterflow 
# but here 
# boundary -> reverse dfs -> mark safe -> convert remaining


# so instead of checking can every 0 reach boundary
# we can reverse it, same as pacific atlantic problem
# we can ask boundary O's --> which O's I can reach 

# boundary O ---> find safe O's 

def solve(board):
    n=len(board)
    m=len(board[0])
    safe=[[False]*m for _ in range(n)]
    dirs=[(0,1),(0,-1),(1,0),(-1,0)]

    def dfs(r,c):
        safe[r][c]=True 
        for dr,dc in dirs:
            nr=r+dr
            nc=c+dc
            if 0<=nr<n and 0<=nc<m:
                if safe[nr][nc]:
                    continue 

                if board[nr][nc]=='O':
                    dfs(nr,nc )

    # start dfs from top row,bottom row,left column,right column 
    # top row
    for j in range(m):
        if board[0][j]=='O' and not safe[0][j]:
            dfs(0,j)

    # bottom row n-1 
    for j in range(m):
        if board[n-1][j]=='O' and not safe[n-1][j]:
            dfs(n-1,j)  

    # left column 0
    for i in range(n):
        if board[i][0]=='O' and not safe[i][0]:
            dfs(i,0)
    
    # right column m-1 
    for i in range(n):
        if board[i][m-1]=='O' and not safe[i][m-1]:
            dfs(i,m-1)

    for i in range(n):
        for j in range(m):
            if board[i][j]=="O" and not safe[i][j]:
                board[i][j]='X'
    return board

print(solve(board))