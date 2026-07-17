# Maximum sum of two non overlapping subarrays
# this is basic level (we can take any length subarrays)

arr=[2,-1,3,4,-5,6]

def maxSum(arr):
    n=len(arr)

    leftMax=[0]*n

    cur=arr[0]
    best=arr[0]
    leftMax[0]=best 
    for i in range(1,n):
        cur=max(arr[i],cur+arr[i])
        best=max(best,cur)

        leftMax[i]=best 

    rightMax=[0]*n 

    best=arr[n-1]
    rightMax[n-1]=best 
    for i in range(n-2,-1,-1):
        cur=max(arr[i],cur+arr[i])
        best=max(best,cur)

        rightMax[i]=best
    
    # try every split
    ans=float('-inf')
    for i in range(n-1):
        candidate=(leftMax[i]+rightMax[i+1])
        ans=max(ans,candidate)
    return ans

print(maxSum(arr))