l=[-1,0,1,2,-1,-4]

def threeSum(l):
    n=len(l)

    l.sort()
    left=0
    right = n-1

    res=[]

    for i in range(n):
        if i>0 and l[i]==l[i-1]:
            continue

        left=i+1
        right=n-1

        while left<right:
            s=l[i]+l[left]+l[right]
            if s<0:
                left+=1