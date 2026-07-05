# Longest subarray with Atmost two distinct integers

arr=[3,1,2,2,2,2]

def longest(arr):
    n=len(arr)
    count={}
    left,max_len=0,0
    for right in range(n):
        count[arr[right]] = count.get(arr[right], 0) + 1
        
        while len(count) > 2:
            count[arr[left]] -= 1
            if count[arr[left]] == 0:
                del count[arr[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    return max_len

print(longest(arr))  # Output: 5 (subarray [2, 2, 2, 2, 1] or [1, 2, 2, 2, 2]
    