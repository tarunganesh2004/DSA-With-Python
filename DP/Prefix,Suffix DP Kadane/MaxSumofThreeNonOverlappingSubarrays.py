# Maximum Sum of 3 Non over lapping subarrays LC 689 (hard)

arr = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2

"""
Left | middle | right 

all three should have fixed length k 

--> leftMax+curWindow+rightMax
so first we find window sums,and then choosing the middle window
if middle window index is i, and length k 
then
left can use upto i-k and right must start from i+k
so best_left+middle(window)+best_right

here window[i]=nums[i:i+k]
"""


def max_sum_of_three_subarrays(nums, k):
    n = len(nums)

    # 1. Calculate every window sum
    window_sum = [0] * (n - k + 1)

    current = sum(nums[:k])
    window_sum[0] = current

    for i in range(k, n):
        current += nums[i]
        current -= nums[i - k]

        window_sum[i - k + 1] = current

    # 2. left_best[i]
    # Best window index from 0 to i

    left_best = [0] * len(window_sum)

    best_index = 0

    for i in range(len(window_sum)):

        if window_sum[i] > window_sum[best_index]:
            best_index = i

        left_best[i] = best_index

    # 3. right_best[i]
    # Best window index from i to end
    right_best = [0] * len(window_sum)

    best_index = len(window_sum) - 1

    for i in range(len(window_sum) - 1, -1, -1):

        if window_sum[i] >= window_sum[best_index]:
            best_index = i

        right_best[i] = best_index

    # 4. Choose every possible middle
    answer = [-1, -1, -1]
    max_total = 0

    for middle in range(k, len(window_sum) - k):

        left = left_best[middle - k]
        right = right_best[middle + k]

        total = window_sum[left] + window_sum[middle] + window_sum[right]

        if total > max_total:
            max_total = total
            answer = [left, middle, right]

    return answer

print(max_sum_of_three_subarrays(arr,k))