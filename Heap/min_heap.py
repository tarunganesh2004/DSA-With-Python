import heapq

def min_heap(arr): # using heapq
    heapq.heapify(arr)
    # heapq.heappush(arr, 0) # push 0 to the heap
    # heapq.heappop(arr) # pop the smallest element from the heap
    return arr

def min_heap_2(arr):
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, i)

    return arr

def heapify(arr, i): # building heap
    left = 2*i + 1
    right = 2*i + 2
    smallest = i

    if left < len(arr) and arr[left] < arr[smallest]:
        smallest = left

    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest)

arr=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(min_heap(arr))
print(min_heap_2(arr))