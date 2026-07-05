l=[5,1,4,2,8]  # noqa: E741
n=len(l)
for i in range(n-1):
    swap=False
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            swap=True

    if not swap:  
        break

print(l)
        