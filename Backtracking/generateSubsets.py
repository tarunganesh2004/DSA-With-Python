arr=[1,2,3]

def generateSubsets(arr): # TC O(n*2^n), SC O(n)
    res=[]
    def backtrack(idx,cur):
        if idx==len(arr):
            res.append(cur[:])
            return
        
        # include the current element
        cur.append(arr[idx])
        backtrack(idx+1,cur)
        cur.pop()

        # exclude the current element
        backtrack(idx+1,cur)
    backtrack(0,[])
    return res

print(generateSubsets(arr)) 