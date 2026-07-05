# Two Sum - Pair with Given Sum

def twoSum(arr,target):
    m={}
    for i in range(len(arr)):
        c=target-arr[i]
        if c in m:
            return [m[c],i] # return True
        
        m[arr[i]]=i
    
    return [-1,-1] # return False

arr = [1, 4, 45, 6, 10, 8]
target=16
print(twoSum(arr,target)) # [3,4]