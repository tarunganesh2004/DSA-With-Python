arr=[5,1,4,2,8,3]

def merge_sort(arr):
    # Binary partition
    if len(arr)<=1:
        return arr
    n=len(arr)
    low=0
    high=n-1
    mid=low+(high-low)//2

    left=merge_sort(arr[low:mid+1])
    right=merge_sort(arr[mid+1:high+1])

    return merge(left,right)

def merge(L,R):
    res=[]
    i=j=k=0

    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            res.append(L[i])
            i+=1
        else:
            res.append(R[j])
            j+=1

    res+=L[i:]
    res+=R[j:]

    return res # TC O(nlogn) SC O(n)

print(merge_sort(arr))