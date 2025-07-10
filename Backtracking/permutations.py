# For Permutations 
# 1. order matters
# 2. we should visit each element exactly once
# 3.We should track which elements are used(using a boolean array)
def permutations(arr):
    res=[]
    n=len(arr)
    used=[False]*n

    def backtrack(cur):
        if len(cur)==n:
            res.append(cur[:])
            return
        for i in range(n):
            if not used[i]: # if the element is not used
                used[i]=True
                cur.append(arr[i])
                backtrack(cur)
                cur.pop()
                used[i]=False # backtrack, mark the element as unused
    backtrack([])
    return res

# permuations with duplicates
def permutations_with_duplicates(arr):
    res=[]
    n=len(arr)
    used=[False]*n
    arr.sort()  # Sort to handle duplicates

    def backtrack(cur):
        if len(cur)==n:
            res.append(cur[:])
            return
        for i in range(n):
            if used[i]:  # if the element is already used
                continue
            if i > 0 and arr[i] == arr[i - 1] and not used[i - 1]:
                continue  # Skip duplicates
            
            used[i]=True
            cur.append(arr[i])
            backtrack(cur)
            cur.pop()
            used[i]=False # backtrack, mark the element as unused
    backtrack([])
    return res

print(permutations([1,2,3]))