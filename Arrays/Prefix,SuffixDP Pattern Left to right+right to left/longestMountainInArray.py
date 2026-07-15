# Longest Mountain In Array LC 845

arr=[2,1,4,7,3,2,5]

"""
this is same as bitonic array but here duplicates are not allowed
so we check strictly increasing and strictly decreasing 

and

here arr is mountain if and only if inc and dec is >1
here inc[i]=1 --> means increasig sequence has length 1, no climb
dec[i]=1 -> no descent
bcz a valid mountain needs atleast one step up and atleast one stepm down
"""

def longestMountain(arr):
    n=len(arr)

    inc=[1]*n 
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            inc[i]=inc[i-1]+1

    dec=[1]*n
    for i in range(n-2,-1,-1):
        if arr[i]>arr[i+1]:
            dec[i]=dec[i+1]+1
    
    ans=0
    for i in range(n):
        if inc[i]>1 and dec[i]>1:
            ans=max(ans,inc[i]+dec[i]-1)
    return ans 

print(longestMountain(arr))