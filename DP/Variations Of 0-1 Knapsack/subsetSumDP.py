arr=[1,2,3]
target=5

# backtracking/recursion
def recursion(arr,cur_ele,target):
    if target==0:
        return True
    if target<0 or cur_ele==len(arr):
        return False
    # include
    include=recursion(arr,cur_ele+1,target-arr[cur_ele])
    # exclude
    exclude=recursion(arr,cur_ele+1,target)
    return include or exclude

print(recursion(arr,0,target)) # O(2^n)


# memoization using lru_cache
from functools import lru_cache  # noqa: E402
@lru_cache(maxsize=None)
def memoization(arr,cur_ele,target):
    if target==0:
        return True
    if target<0 or cur_ele==len(arr):
        return False
    # include
    include=memoization(arr,cur_ele+1,target-arr[cur_ele])
    # exclude
    exclude=memoization(arr,cur_ele+1,target)
    return include or exclude
print(memoization(tuple(arr),0,target)) # O(n*target)

# memoization using 2d array
def memoization_2d(arr, cur_ele, target, dp):
    if target==0:
        return True
    if target<0 or cur_ele==len(arr):
        return False
    if dp[cur_ele][target] != -1:
        return dp[cur_ele][target]
    # include
    include = memoization_2d(arr, cur_ele + 1, target - arr[cur_ele], dp)
    # exclude
    exclude = memoization_2d(arr, cur_ele + 1, target, dp)
    dp[cur_ele][target] = include or exclude
    return dp[cur_ele][target]

dp=[[-1]*(target+1) for _ in range(len(arr)+1)]
print(memoization_2d(arr, 0, target, dp)) # O(n*target)

# dynamic programming tabulation
def subset_sumdp(arr,target):
    # dp[i][j] will be True if a subset with sum j can be formed using the first i elements
    n=len(arr)
    dp=[[False]*(target+1) for _ in range(n+1)] # O(n*target)
    for i in range(n+1):
        dp[i][0] = True  # A sum of 0 can always be formed with an empty subset
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]

print(subset_sumdp(arr, target))  # O(n*target)

# space optimized dynamic programming
def subset_sumdp_space_optimized(arr, target):
    n = len(arr)
    dp = [False] * (target + 1)
    dp[0] = True  # A sum of 0 can always be formed with an empty subset
    for i in range(n):
        for j in range(target, arr[i] - 1, -1):
            dp[j] = dp[j] or dp[j - arr[i]]
    return dp[target]
print(subset_sumdp_space_optimized(arr, target))  # O(n*target) with O(target) space