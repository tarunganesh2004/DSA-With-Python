# Maximum sum bitonic subarray

# this is same as longest bitonic subarray
# there we stored lengths
# here we store sum in inc and dec arrays

arr=[1,3,5,4,2]

arr = [1, 3, 5, 4, 2]


def maxSumBitonic(arr):

    n = len(arr)

    inc = arr[:]

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc[i] = inc[i - 1] + arr[i]

    dec = arr[:]

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            dec[i] = dec[i + 1] + arr[i]

    ans = 0

    for i in range(n):
        ans = max(ans, inc[i] + dec[i] - arr[i])

    return ans


print(maxSumBitonic(arr))