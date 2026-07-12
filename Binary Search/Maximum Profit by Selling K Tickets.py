# Max Amount By Selling K Tickets

arr = [4, 3, 6, 2, 4]
k = 3

# brute force is O(n*k),iterating k times array and finding seller with max tickets


def bruteForce(arr, k):
    ans = 0

    while k > 0:
        idx = 0

        for i in range(1, len(arr)):
            if arr[i] > arr[idx]:
                idx = i

        # it ticket is 0 ,no tickets left anywhere
        if arr[idx] == 0:
            break

        # sell one ticket
        ans += arr[idx]

        arr[idx] -= 1  # remaining tickets decrease
        k -= 1
    return ans


# print(bruteForce(arr,k))


# another approach is instead of finding maximum seller everytime
# we can use maxheap --> so O(n+klogn)
import heapq


def anotherApproachUsingHeap(arr, k):

    n = len(arr)
    mod = 10**9 + 7
    heap = [-x for x in arr]
    heapq.heapify(heap)

    ans = 0
    while k > 0 and heap:

        # get max
        cur = -heapq.heappop(heap)

        ans = (ans + cur) % mod

        cur -= 1
        k -= 1

        # push if tickets remaining
        if cur > 0:
            heapq.heappush(heap, -cur)

    return ans


print(anotherApproachUsingHeap(arr, k))


# optimized approach is binary search
class Solution:
    def maxProfit(self, arr, k):
        MOD = 10**9 + 7

        low = 0
        high = max(arr)

        while low <= high:
            mid = (low + high) // 2

            sold = 0
            for x in arr:
                if x > mid:
                    sold += x - mid

            if sold >= k:
                low = mid + 1
            else:
                high = mid - 1

        level = high

        ans = 0
        sold = 0

        for x in arr:
            if x > level:
                cnt = x - level
                sold += cnt

                ans += (x + level + 1) * cnt // 2

        extra = sold - k

        ans -= extra * (level + 1)

        return ans % MOD


s=Solution()
print(s.maxProfit(arr,k))