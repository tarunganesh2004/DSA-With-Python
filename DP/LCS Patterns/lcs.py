# Longest common subsequence DP
A = [1, 3, 4, 1]
B = [3, 4, 1, 2, 1, 3]
# bruteforce
def recursion(arr1,arr2):
    m,n=len(arr1),len(arr2)
    def f(i,j):
        if i==m or j==n:
            return 0
        
        if arr1[i]==arr2[j]:
            return 1+f(i+1,j+1) # keep that element and go to next 
        
        return max(f(i+1,j),f(i,j+1)) # skip a[i], or skip b[j] take maximum of both
    
    return f(0,0)

# memoization
def memoization(A,B):
    m,n=len(A),len(B)
    dp=[[-1]*(n+1) for _ in range(m+1)]

    def f(i,j):
        if i==m or j==n:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        

        if A[i]==B[j]:
            dp[i][j]=1+f(i+1,j+1)
        else:
            dp[i][j]=max(f(i+1,j),f(i,j+1))
        return dp[i][j]
    return f(0,0)

# tabulation
def tabulation(A,B):
    m,n=len(A),len(B)

    # so size (m+1)*(n+1) , since dp[i][j] depends on dp[i+1][j+1],dp[i+1][j],dp[i][j+1]
    # we must fill bottom to top, and right to left
    dp = [[0] * (n + 1) for _ in range(m+ 1)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if A[i]==B[j]:
                dp[i][j]=1+dp[i+1][j+1]
            
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])

    return dp[0][0]

print(recursion(A,B))
print(memoization(A,B))
print(tabulation(A,B))


"""
so for qsns like minimum insertions and deletions,
Whenever you see:

make two sequences equal
minimum insertions/deletions
same order must be preserved

Think:

What is the maximum part I can keep?

↓

Longest Common Subsequence
Similar Problems
Minimum Insertions and Deletions.
Delete Operation for Two Strings.
Uncrossed Lines.
Shortest Common Supersequence.
Minimum ASCII Delete Sum.
Distinct Subsequences.
Edit Distance.

"""
