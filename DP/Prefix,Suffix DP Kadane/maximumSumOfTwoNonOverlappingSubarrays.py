# Maximum Sum of Two Non Overlapping Subarrays LC 1031
"""

if they asking directly for any different length subarrays
we can solve from previous problem(max absolute difference)
using leftMax and rightMax, max(ans,leftMax[i]+rightMax[i])

but here they asked
subarray lengths should be L & M they mentioned

before left subarray | right subarray 

now we have 2 cases firstLen comes first

L-subarray | M-subarray --> bestL+bestM

case2: secondLen comes first

M-subarray | L-subarray --> bestM+bestL

here we dont unse kadane bcz subarray lengths are fixed

"""
nums=[0,6,5,2,2,5,1,9,4]
firstLen=1
secondLen=2

def maxSumTwoNoOverlap(nums,firstLen,secondLen):
    n=len(nums)

    # max sum of 1st len window in every prefix
    left_first=[0]*n 

    # max sum of 2nd len window in every prefix 
    left_second=[0]*n 

    # max sum of 1st len window in every suffix
    right_first=[0]*n

    # max sum of 2nd len window in every suffix
    right_second=[0]*n 

    # prefix maximum windows of length firstLen
    window_sum=sum(nums[:firstLen])
    left_first[firstLen-1]=window_sum
    for i in range(firstLen,n):
        window_sum+=nums[i]
        window_sum-=nums[i-firstLen]

        left_first[i]=max(left_first[i-1],window_sum)

    # prefix maximum windows of length secondLen
    window_sum=sum(nums[:secondLen])
    left_second[secondLen-1]=window_sum

    for i in range(secondLen,n):
        window_sum+=nums[i]
        window_sum-=nums[i-secondLen]

        left_second[i]=max(left_second[i-1],window_sum)

    # suffix maximum windows of length firstLen
    window_sum=sum(nums[n-firstLen:])
    right_first[n-firstLen]=window_sum
    for i in range(n-firstLen-1,-1,-1):
        window_sum+=nums[i]
        window_sum-=nums[i+firstLen]
        
        right_first[i]=max(right_first[i+1],window_sum)
    
    # suffix maximum windows of length secondLen 
    window_sum=sum(nums[n-secondLen:])
    right_second[n-secondLen]=window_sum
    for i in range(n-secondLen-1,-1,-1):
        window_sum+=nums[i]
        window_sum-=nums[i+secondLen]

        right_second[i]=max(right_second[i+1],window_sum)
    
    # try every split
    ans=float('-inf')
    for i in range(n-1):
        # firstLen subrray before secondlen subarray
        if i>=firstLen-1 and i+1<=n-secondLen:
            ans=max(ans,left_first[i]+right_second[i+1])

        # second len subarray before firsLen subarray
        if i>=secondLen-1 and i+1<=n-firstLen:
            ans=max(ans,left_second[i]+right_first[i+1])
        
    return ans 

print(maxSumTwoNoOverlap(nums,firstLen,secondLen))