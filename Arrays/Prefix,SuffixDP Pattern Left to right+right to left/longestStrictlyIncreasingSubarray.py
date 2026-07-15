# Longest Strictly Increasing Subarray 

arr=[1,2,3,2,5,6,7,1]

def longestIncreasing(arr):
    n=len(arr)

    cur=1
    ans=1
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            cur+=1
        else:
            cur=1
        ans=max(cur,ans)
    return ans 

print(longestIncreasing(arr))

arr1=[9,8,7,6,2,5,4,3]
# longest Strictly Decreasing subarray 
def longestDecreasing(arr):
    cur=1
    ans=1 
    n=len(arr)
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            cur+=1
        else:
            cur=1
        
        ans=max(ans,cur)
    return ans 

print(longestDecreasing(arr1))