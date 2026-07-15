# Trapping Rain Water LC 42 (Hard)

height=[0,1,0,2,1,0,1,3,2,1,2,1]
"""
This is similar to bitonic array problem
Bitonic

Left
inc[]
Right
dec[]
Merge
inc+dec-1

+
------------------
Rain Water

Left
leftMax[]
Right
rightMax[]
Merge
min()-height

so for every index we need highest wall on the left and highest wall on right
then water=min(leftMax,rightMax)-height
"""

def trap(height):
    n=len(height)
    # left max
    # leftMax[i] = Maximum wall height seen from the left up to index i (including i).
    leftMax=[0]*n 
    leftMax[0]=height[0]
    for i in range(1,n):
        leftMax[i]=max(leftMax[i-1],height[i])

    # rightMax
    # rightMax[i] -->Maximum height of any wall from index i to the end (including i).
    rightMax=[0]*n
    rightMax[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        rightMax[i]=max(rightMax[i+1],height[i])

    ans=0
    for i in range(n):
        ans+=min(leftMax[i],rightMax[i])-height[i]

    return ans 

# space optimized
def spaceOptimized(arr):
    n=len(arr)
    left,right=0,n-1
    leftMax,rightMax=0,0
    ans=0

    while left<=right:
        if arr[left]<=right:
            if arr[left]<leftMax:
                ans+=leftMax-arr[left]
            else:
                leftMax=arr[left]
            left+=1

        else:
            if arr[right]<rightMax:
                ans+=rightMax-arr[right]
            else:
                rightMax=arr[right]
            right-=1

    return ans

print(trap(height))
