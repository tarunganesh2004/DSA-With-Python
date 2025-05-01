p=[5,6,2]
w=[3,4,1]
cap=6

def knapsack(w,p,cap,n):
    if n==0 or cap==0:
        return 0
    if w[n-1]>cap:
        # skip
        return knapsack(w,p,cap,n-1)
    
    else:
        # include
        return max(knapsack(w,p,cap,n-1),p[n-1]+knapsack(w,p,cap-w[n-1],n-1))
    
print(knapsack(w,p,cap,len(p)))