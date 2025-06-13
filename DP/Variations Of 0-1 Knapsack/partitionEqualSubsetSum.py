# Parition Equal Subset Sum Problem

# It is a variation of the 0-1 Knapsack problem where we need to find if we can partition the given set into two subsets such that the sum of elements in both subsets is equal.
# it is similar to the subset sum problem where we need to find if there is a subset with sum equal to target/2

nums=[1,5,11,5] # if total sum is odd, we cannot partition it into two equal subsets
# so target=sum(nums)//2

# recursion 
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

print(recursion(nums,0,sum(nums)//2)) # O(2^n)

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

print(memoization(tuple(nums),0,sum(nums)//2)) # O(n*target)

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

target=sum(nums)//2
dp=[[-1]*(target+1) for _ in range(len(nums)+1)]
print(memoization_2d(nums, 0, target, dp)) # O(n*target)