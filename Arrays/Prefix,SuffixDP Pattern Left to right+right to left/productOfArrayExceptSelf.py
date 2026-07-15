# Product of array except self LC 238

nums=[1,2,3,4]

def productExceptSelf(nums):
    n=len(nums)
    l=[1]*n 

    left=1
    for i in range(n):
        l[i] = left  # product of all elements to the left of index i(excluding nums[i])
        left=left*nums[i]

    right=1
    r=[1]*n 
    for i in range(n-1,-1,-1):
        r[i]=right
        right=right*nums[i]

    res=[1]*n 
    for i in range(n):
        res[i]=l[i]*r[i]
    return res


# O(1) space
def optimize(l):
    n = len(l)
    r = [1] * n

    left = 1
    for i in range(n):
        r[i] = left
        left = left * l[i]

    right = 1
    for i in range(n - 1, -1, -1):
        r[i] *= right
        right *= l[i]
    return right 

print(productExceptSelf(nums))
