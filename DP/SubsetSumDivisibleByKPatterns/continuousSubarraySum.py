# LC 523, Continuous Subarray sum
# before we checked for subset

nums=[23,2,4,6,7]
k=6

# BruteForce
def bruteForce(nums,k):
    n=len(nums)
    for i in range(n):
        sm=0
        for j in range(i,n):
            sm+=nums[j]
            if j-i+1>=2 and sm%k==0:
                return True 
    return False

"""
prefix[j]%k=prefix[i]%k
(prefix[j]-prefix[i])%k=0
means sum(i+1....j) is divisible by k
"""
# so store remainders, remainder --> 1st index
def checkSubarraysum(nums,k):
    n=len(nums)
    prefix=0
    mp={0:-1}
    for i in range(n):
        prefix+=nums[i]
        rem=prefix%k

        if rem in mp:
            if i-mp[rem]>=2:
                return True
        else:
            mp[rem]=i

    return False 

print(checkSubarraysum(nums,k))

"""
Pattern
Existence Question
+
Subarray divisible by k
↓
Store first occurrence of remainder.
"""
