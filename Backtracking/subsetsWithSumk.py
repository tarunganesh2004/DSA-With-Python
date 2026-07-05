# Find Subsets with sum k 

arr=[1,2,3]
k=3

def subset_sum_k(arr,k):
    res=[]
    count=0

    def backtrack(index,current,sum_so_far):
        nonlocal count
        if index==len(arr):
            if sum_so_far == k:
                res.append(current[:])
                count+=1
            return
        
        # pick 
        current.append(arr[index])
        backtrack(index + 1, current, sum_so_far + arr[index])
        current.pop()

        # not pick
        backtrack(index + 1, current, sum_so_far)
    backtrack(0, [], 0)
    return res,count

# Subsets with sum k without duplicates
def subset_sum_k_no_duplicates(arr, k):
    res=[]
    arr.sort()  # Sort to handle duplicates

    def backtrack(index,cur,sum_so_far):
        if sum_so_far== k:
            res.append(cur[:])
            return
        
        for i in range(index,len(arr)):
            if i > index and arr[i] == arr[i - 1]:
                continue # Skip duplicates

            if sum_so_far+arr[i]>k:
                break 

            cur.append(arr[i])
            backtrack(i + 1, cur, sum_so_far + arr[i])
            cur.pop()
    backtrack(0, [], 0)
    return res

print(subset_sum_k(arr, k))  # Output: [[1, 2], [3]]