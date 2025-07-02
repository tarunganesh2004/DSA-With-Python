# https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1

x=51
arr=[1, 4, 45, 6, 0, 19]

def smallestSubarraySumGreaterthanx(arr, x):
    if sum(arr)<x:
        return 0
    n=len(arr)
    min_len=n+1
    cur_sum=0
    start=0
    end=0
    while end<n:
        while cur_sum<=x and end<n:
            cur_sum+=arr[end]
            end+=1

        while cur_sum>x and start<n: # shrink the window
            min_len=min(min_len, end-start)
            cur_sum-=arr[start]
            start+=1
    return min_len

print(smallestSubarraySumGreaterthanx(arr, x))