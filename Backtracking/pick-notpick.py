# pick not pick pattern 

def recurse(index,cur):
    if index==len(arr):
        print(cur)
        return 
    # pick the current element
    cur.append(arr[index])
    recurse(index+1,cur)
    cur.pop() # backtrack

    # not pick the current element
    recurse(index+1,cur)

arr=[1,2,3]
recurse(0,[]) # prints all subsets of the array