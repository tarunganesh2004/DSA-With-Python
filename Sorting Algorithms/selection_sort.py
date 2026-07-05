# Selection sort is a simple sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list., TC O(n^2) SC O(1)
arr=[5,1,4,2,8]

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        print(f"Iteration {i + 1}, initial array: {arr}")
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Swapping index {i} and min index {min_idx}: {arr}")

    return arr

print(selection_sort(arr)) # [1, 2, 4, 5, 8]
