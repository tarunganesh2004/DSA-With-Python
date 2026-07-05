# LC 974,Subarray Sums divisble by k

# bruteforce O(n^2)
# previous(continous subarrays sum they asked need existence) now we need count

# so here we use remainder,frequency map

nums=[4,5,0,-2,-3,1]
k=5

def subarraysDivByK(nums,k):
    cnt={0:1}
    prefix=0
    ans=0

    for num in nums:
        prefix+=num

        rem=prefix%k 
        
        ans+=cnt.get(rem,0)

        cnt[rem]=cnt.get(rem,0)+1
    
    return ans 

print(subarraysDivByK(nums,k))

"""
Pattern Learnt 
Count Question
+
Subarray divisible by k
↓
Store frequencies of remainders.
"""
