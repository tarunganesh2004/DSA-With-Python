wt=[1,3,4]
profits=[15,20,30]
W=4

def recursive(wt,profits,W):
    n=len(wt)
    # Maximum profit obtainable using items from index i onward with remaining capacity cap.
    def solve(i,cap):
        if i==n:
            return 0
        
        # skip
        not_take=solve(i+1,cap)
        take=0
        if wt[i]<=cap:
            take=profits[i]+solve(i+1,cap-wt[i])

        return max(take,not_take)
    
    return solve(0,W)


def memoization(wt,profits,W):
    n=len(wt)

    dp=[[-1]*(W+1) for _ in range(n)]

    def solve(i,cap): # this reduces to O(nW) TC
        if i==n:
            return 0
        
        if dp[i][cap]!=-1:
            return dp[i][cap]
        
        not_take=solve(i+1,cap)
        take=0
        if wt[i]<=cap:
            take=profits[i]+solve(i+1,cap-wt[i])

        dp[i][cap]=max(take,not_take)

        return dp[i][cap]
    
    return solve(0,W)