# NQueens 

n=4

def nqueens(n):
    board=[["."]*n for _ in range(n)]
    cols=set()
    diag=set() # r-c
    anti = set() # r+c 

    res=[]

    def dfs(row):
        if row==n:
            res.append(["".join(r) for r in board])
            return 
        
        for col in range(n):
            # not safe 
            if col in cols or row-col in diag or row+col in anti:
                # skip
                continue

            #choose
            cols.add(col)
            diag.add(row-col)
            anti.add(row+col)

            board[row][col]="Q"

            dfs(row+1)

            # backtrack
            board[row][col]="."
            
            cols.remove(col)
            diag.remove(row-col)
            anti.remove(row+col)
    dfs(0)
    return res 

print(nqueens(n))