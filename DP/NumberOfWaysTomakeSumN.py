# Ways to write n as sum of two or more positive Integers

n=5 # 6ways
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# brute force recursion
MOD=10**9+7

def bruteForce(n):
    from functools import lru_cache
    @lru_cache(None)
    def solve(num,rem):
        if rem==0:
            return 1
        if num>rem:
            return 0
        
        take=solve(num,rem-num)
        skip=solve(num+1,rem)

        return take+skip 
    
    return solve(1,n)-1 # -1 because we need here sum of two or more integers

# memoization
def memoization(n):
    memo={}
    def solve(num,rem):
        if rem==0:
            return 1
        
        if num>rem:
            return 0
        
        if (num,memo) in memo:
            return memo[(num,rem)]
        
        take=solve(num,rem-num)
        skip=solve(num+1,rem)

        memo[(num,rem)]=(take+skip)%MOD

        return memo[(num,rem)]
    
    return (solve(1,n)-1)%MOD 

# dp
def dp(n):
    MOD=10**9+7
    dp=[[0]*(n+1) for _ in range(n+2)] # num ranges from 1 to n+1, rem ranges from 0 to n 
    for num in range(n+2):
        dp[num][0]=1

    for num in range(n,0,-1):
        for rem in range(1,n+1):
            skip=dp[num+1][rem]

            take=0
            if rem>=num:
                take=dp[num][rem-num]

            dp[num][rem]=(take+skip)%MOD
        
    return (dp[1][n]-1)%MOD
        

print(bruteForce(n))