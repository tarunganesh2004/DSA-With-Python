# Word Search LC 79
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

def exist(board,word):
    n,m=len(board),len(board[0])
    vis=[[False]*m for _ in range(n)]

    def dfs(r,c,i):
        if i==len(word):
            return True 
        
        if r<0 or r>=n or c<0 or c>=m or board[r][c]!=word[i] or vis[r][c]:
            return False 
        
        vis[r][c]=True 

        res=(
            dfs(r+1,c,i+1) or dfs(r-1,c,i+1)
            or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
        )

        vis[r][c]=False 
        return res 
    
    for r in range(n):
        for c in range(m):
            if dfs(r,c,0) and board[r][c]==word[0]: # starting character of string
                return True 
            
    return False 

print(exist(board,word))