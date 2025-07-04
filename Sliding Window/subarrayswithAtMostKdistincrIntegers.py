# Subarrays with at most K distinct integers

arr=[1,2,2,3]
k=2

def subarraysWithAtMostKDistinct(arr, k):
    from collections import defaultdict
    n = len(arr)
    left=0
    count=defaultdict(int)
    subarray_count=0
    for right in range(n):
        count[arr[right]]+=1

        while len(count)>k:
            count[arr[left]]-=1
            if count[arr[left]]==0:
                del count[arr[left]]
            left+=1

        subarray_count += right - left + 1
    return subarray_count

print(subarraysWithAtMostKDistinct(arr, k))  # Output: 9