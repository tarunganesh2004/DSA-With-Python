# Length of the longest substring without repeating characters

s="abcabcbb"

def longest(s):
    n=len(s)
    S=set()
    res=0
    start=0
    end=0

    while end<n:
        if s[end] not in S:
            S.add(s[end])
            end+=1
            res=max(res,end-start)
        else:
            S.remove(s[start])
            start+=1
        
    return res

print(longest(s)) # 3