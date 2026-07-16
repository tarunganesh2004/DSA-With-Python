# Count Binary Strings without consecutive Ones 

"""
this is opposite of count binary strings with exactly k consecutive ones

but here in the recursion state, at position i, we need prev position character also 

upto before problems dfs(i,accumulated_state)

now this problem dfs(i,previous_choice)

if prev_bit is 0, then we can place 0 or 1, dfs(i+1,0) ,dfs(i+1,1)
if prev_bit is 1, then we can place 0 --> transition dfs(i+1,0)
"""

n=3

# this problem position dp+previous choice
# brute force
def recursion(n):

    def dfs(i,prev_bit):
        if i==n:
            return 1
        
        if prev_bit==1:
            return dfs(i+1,0)
        else:
            return (dfs(i+1,0)+dfs(i+1,1))
        
    return dfs(0,0)

# memoization
def memoization(n):
    memo=[[-1]*2 for _ in range(n+1)]
    def dfs(i,prev_bit):
        if i==n:
            return 1
        if memo[i][prev_bit]!=-1:
            return memo[i][prev_bit]
        
        if prev_bit==1:
            ans=dfs(i+1,0)
        else:
            ans=(dfs(i+1,1)+dfs(i+1,0))
        
        memo[i][prev_bit]=ans 
        return ans 
    
    return dfs(0,0)

# tabulation
def tabulation(n):
    dp=[[0]*2 for _ in range(n+1)]
    # base cases,if i==n then return 1, so both possible previous bits are valid when the string is complete
    dp[n][0]=1
    dp[n][1]=1

    for i in range(n-1,-1,-1):
        
        # prev bit 1
        dp[i][1]=dp[i+1][0]

        # prev bit 0
        dp[i][0]=dp[i+1][0]+dp[i+1][1]
    return dp[0][0]

print(recursion(n))
print(memoization(n))
print(tabulation(n))