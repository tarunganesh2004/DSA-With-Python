l=[1,1,3,1,5 ,6,1,1,1,1,1,1,1,1]
n=len(l)

count=0
max_count=0
for i in range(n):
    if l[i]==1:
        count+=1
        max_count=max(count,max_count)
    else:
        count=0

print(max_count)