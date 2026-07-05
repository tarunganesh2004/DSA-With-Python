from collections import deque
arr=[100,200,300,400]
k=2

def maxSubarray(arr,k):
    n=len(arr)
    cur_sum=0
    max_sum=0
    start=0
    end=0
    while end<n:
        while end<n and end-start<k:
            cur_sum+=arr[end]
            end+=1
        
        max_sum=max(max_sum, cur_sum)
        cur_sum-=arr[start]
        start+=1

    return max_sum

def anotherWaySliding(arr,k):
    if len(arr)<k:
        return -1
    
    res=0
    for i in range(k):
        res+=arr[i]

    cur_sum=res
    for i in range(k,len(arr)):
        cur_sum+=arr[i]-arr[i-k]
        res=max(res,cur_sum)

    return res

print(maxSubarray(arr,k)) # 700
# print(anotherWay(arr,k)) # 700

def minSubarray(arr,k):
    n=len(arr)
    if n<k:
        return -1
    
    res=0
    for i in range(k):
        res+=arr[i]

    cur_sum=res
    for i in range(k,len(arr)):
        cur_sum+=arr[i]-arr[i-k]
        res=min(res,cur_sum)
    
    return res

print(minSubarray(arr,k)) # 300

def anotherWay(arr,k):
    if len(arr)<k:
        return -1
    # by using deque
    # first push k elements into deque and calculate the sum while pushing
    # then pop the leftmost element and push the next element and calculate the sum
    # update the result

    n=len(arr)
    q=deque()

    # initialize maximum and cur_sum
    m=float('-inf')
    cur_sum=0

    for i in range(k):
        q.append(arr[i])
        cur_sum+=arr[i]

    for i in range(k,n):
        m=max(m,cur_sum)
        
        # remove the first element from the deque
        cur_sum-=q[0]
        q.popleft()

        # add the next element to the deque
        q.append(arr[i])
        cur_sum+=arr[i]

    m=max(m,cur_sum)
    return m

print(anotherWay(arr,k)) # 700