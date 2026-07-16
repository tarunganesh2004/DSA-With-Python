# Count Binary Strings with exactly K ones

N=3
k=2

# recursion
def bruteForce(n,k):

    def dfs(i,ones_count):
        if i==n:
            return 1 if k==ones_count else 0
        
        # place 0
        takeZero=dfs(i+1,ones_count)

        # place 1
        takeOne=dfs(i+1,ones_count+1)

        return takeZero+takeOne
    
    return dfs(0,0)

# memoization
def memoization(n,k):
    memo=[[-1]*(k+1) for _ in range(n+1)]

    def dfs(i,ones):
        if ones>k:
            return 0
        
        if i==n:
            return 1 if ones==k else 0
        
        if memo[i][ones]!=-1:
            return memo[i][ones]
        
        takeZero=dfs(i+1,ones)
        takeOne=dfs(i+1,ones+1)

        memo[i][ones]=takeOne+takeZero

        return memo[i][ones]
    return dfs(0,0)

def tabulation(n,k):
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[n][k]=1
    for i in range(n-1,-1,-1):
        for ones in range(k,-1,-1):
            ans=dp[i+1][ones] # place 0

            if ones+1<=k:
                ans+=dp[i+1][ones+1]
            
            dp[i][ones]=ans
    return dp[0][0]


print(bruteForce(N,k))
print(memoization(N,k))
print(tabulation(N,k))

"""
Ternary strings with k twos --> same pattern
but here we have 3 cases
takeo=dfs(i+1,c2)
take1=dfs(i+1,c2)
take2=dfs(i+1,c2+1)
"""