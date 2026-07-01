# maximum subarray sum


arr=[1,2,3,-4,5]

# def kadane(arr): # general approach
#     n=len(arr)
#     cur_sum=0
#     max_sum=float('-inf')
#     for num in arr:
#         cur_sum+=num
#         max_sum=max(cur_sum,max_sum)
#         if cur_sum<0:
#             cur_sum=0
#     return max_sum

# recursion function
# f(i)=maximum subarray sum ending at index i
def kadane_recursive(arr):
    ans=float('-inf')
    def f(i,arr):
        if i==0:
            return arr[0]
        return max(arr[i],arr[i]+f(i-1,arr))
    for i in range(len(arr)):
        ans=max(ans,f(i,arr))
    return ans 

# dp version(tabulation)
def kadanedp(arr):
    n=len(arr)
    dp=[0]*n 
    dp[0]=arr[0]
    ans=dp[0]
    for i in range(1,n):
        dp[i]=max(arr[i],dp[i-1]+arr[i])
        ans=max(ans,dp[i])
    return ans 

def kadaneoptimized(arr): # space optimized dp--> actual kadane
    cur_sum=0
    max_sum=0
    for i in range(1,len(arr)):
        # dp version is 
        '''
        dp[i]=max(
        arr[i], # start new subarray
        dp[i-1]+arr[i] # extended previous subarray
        )
        '''
        cur_sum=max(arr[i],cur_sum+arr[i])
        max_sum=max(max_sum,cur_sum)
    return max_sum 


"""
Recursion
f(i) = max(arr[i], arr[i] + f(i-1))
           ↓
Memoization
           ↓
Tabulation
           ↓
Space Optimization
           ↓
Kadane Algorithm
"""
