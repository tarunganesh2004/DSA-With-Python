import heapq

def max_heap(arr):
    # use negative values to simulate max heap
    arr=[-x for x in arr]
    heapq.heapify(arr)
    return [-x for x in arr]

def max_heap_2(arr):
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, i)

    return arr

def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    # Compare left child
    if left < len(arr) and arr[left] > arr[largest]:
        largest = left

    # Compare right child
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the current node, swap and heapify further
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

arr=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(max_heap(arr))
print(max_heap_2(arr))