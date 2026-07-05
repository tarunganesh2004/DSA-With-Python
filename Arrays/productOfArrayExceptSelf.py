l=[1,2,3,4]

def product(l):
    n=len(l)
    r=[1]*n

    left=1
    for i in range(n):
        r[i]=left
        left=left*l[i]

    right=1
    for i in range(n-1,-1,-1):
        r[i]*=right
        right*=l[i]
    print(r)
    print()

product(l)