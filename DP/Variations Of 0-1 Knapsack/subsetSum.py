# Subset Sum problem 
# Can we form a subset with sum=target
# this is a variation of the 0-1 knapsack problem , here we need not to maximize the profit but just check if we can form a subset with sum=target

arr=[3,34,4,12,5,2]
target=9

# recursion
def recursive(arr,n,target):
    if target==0:
        return True
    if n==0:
        return False
    
    if arr[n-1]>target:
        # skip the item
        return recursive(arr,n-1,target)
    # include or exclude the item
    return recursive(arr, n - 1, target - arr[n - 1]) or recursive(arr, n - 1, target) 

# using memoization(lru_cache)
from functools import lru_cache  # noqa: E402
def memoi(arr,n,target):
    arr=tuple(arr)
    @lru_cache(None)
    def dfs(i,target):
        if target==0:
            return True
        if i==0:
            return False
        
        if arr[i-1]>target:
            # skip the item
            return dfs(i-1,target)
        # include or exclude the item
        return dfs(i-1,target-arr[i-1]) or dfs(i-1,target)
    
    return dfs(n,target)

# memoization with map or 2d array(Top Down DP)
# memoization with map (top-down DP)
def memo(arr, n, target, memo_dict):
    if target == 0:
        return True
    if n == 0:
        return False
    if (n, target) in memo_dict:
        return memo_dict[(n, target)]
    if arr[n - 1] > target:
        memo_dict[(n, target)] = memo(arr, n - 1, target, memo_dict)
    else:
        include = memo(arr, n - 1, target - arr[n - 1], memo_dict)
        exclude = memo(arr, n - 1, target, memo_dict)
        memo_dict[(n, target)] = include or exclude
    return memo_dict[(n, target)]

print(recursive(arr,len(arr),target))
print(memoi(arr,len(arr),target))

memo_dict={}
print(memo(arr,len(arr),target,memo_dict))

# DP (Tabulation) bottom up approach
def dp(arr,target): # O(n*target) time and O(n*target) space
    # create a 2D array of size (n+1)*(target+1)
    n=len(arr)
    dp=[[False]*(target+1) for _ in range(n+1)]

    # sum with 0 is always possible
    for i in range(n+1):
        dp[i][0]=True

    for i in range(1,n+1):
        for j in range(1,target+1):
            # if the current element is greater than the target, we can't include it
            if arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                # include or exclude the current element
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
    
    return dp[n][target]

print(dp(arr,target))

# DP (Tabulation) bottom up approach with 1D array
def dp1D(arr,target): # O(n*target) time and O(target) space
    n=len(arr)
    dp=[False]*(target+1)

    # sum with 0 is always possible
    dp[0]=True

    for i in range(1,n+1):
        for j in range(target,-1,-1):
            # if the current element is greater than the target, we can't include it
            if arr[i-1]>j:
                continue
            else:
                # include or exclude the current element
                dp[j]=dp[j-arr[i-1]] or dp[j]
    
    return dp[target]

print(dp1D(arr,target))