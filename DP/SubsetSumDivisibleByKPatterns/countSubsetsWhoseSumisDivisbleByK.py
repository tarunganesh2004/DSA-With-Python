# this is extended version of subsetsum divisble k

# same as take ,not take approach
# f(i,rem)
# for non empty subset modification
# add a new variable taken or count all subsets and subtract empty subset(f(0,0)-1)

# memoization
def countSubsetDivisble(arr,k):
    n=len(arr)
    dp=[[-1]*k for _ in range(n+1)]

    def f(i,rem):
        if i==n:
            return 1 if rem==1 else 0
        
        if dp[i][rem]!=-1:
            return dp[i][rem]
        
        take=f(i+1,(rem+arr[i])%k)
        notTake=f(i+1,rem)

        dp[i][rem]=take+notTake 

        return dp[i][rem]
    
    return f(0,0)-1

# space optimized version
# instead of storing possible remainders, count ways to obtain remainder r

def optimized(arr,k):
    dp=[0]*k 
    dp[0]=1


    for num in arr:
        ndp=dp[:]
        for r in range(k):
            nr=(r+num)%k 
            ndp[nr]+=dp[r]
        
        dp=ndp 
    
    return dp[0]-1
