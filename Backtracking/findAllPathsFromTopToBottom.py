# https://www.geeksforgeeks.org/problems/find-all-possible-paths-from-top-to-bottom/1?page=2&category=Backtracking&sortBy=submissions

# Given a N x M grid. Find All possible paths from top left to bottom right.From each cell you can either move only to right or down.

mat=[
    [1,2,3],
    [4,5,6]
]
# output : 1 4 5 6, 1 2 5 6, 1 2 3 6

def findAllpathsFromTopToBottom(mat): # TC O(2^(n+m)), SC O(n+m)
    n=len(mat)
    m=len(mat[0])
    res,curPath,i,j=[],[],0,0

    def dfs(n,m,i,j,res,curPath,mat):
        if i>=n or j>=m:
            return
        
        # add current cell to the path
        curPath.append(mat[i][j])
        if i==n-1 and j==m-1:
            res.append(curPath[:]) # if reached the bottom right cell, add the path to the result
            
        # move down
        dfs(n, m, i + 1, j, res, curPath, mat)
        # move right
        dfs(n,m,i,j+1,res,curPath,mat)
        
        curPath.pop() # remove the last element to backtrack
    
    dfs(n,m,i,j,res,curPath,mat)
    for i in range(len(res)):
        print(" ".join(map(str,res[i])))
    return res

print(findAllpathsFromTopToBottom(mat)) # [[1, 2, 5, 6], [1, 4, 5, 6], [1, 2, 3, 6]]
