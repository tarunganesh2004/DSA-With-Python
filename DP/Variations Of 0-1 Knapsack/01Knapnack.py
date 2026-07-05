# profits=[4,4,7,1]
# weights=[5,2,3,1]
# capacity =8
# so output is 7+4+1=12

p=[4,4,7,1]
w=[5,2,3,1]
c=8

def maxProfit(p,w,c):
    # store p,w in pairs
    pw=[]
    for i in range(len(p)):
        pw.append((p[i],w[i]))
    # print(pw)

    # sort the pw in descending order of profit/weight
    pw.sort(key=lambda x:x[0]/x[1],reverse=True)
    # print(pw)
    max_profit=0
    remaining_capacity=c
    for price,weight in pw:
        if weight<=remaining_capacity:
            max_profit+=price
            remaining_capacity-=weight
        else:
            break # 0-1 knapsack, so we can't take fraction of an item

    print(max_profit)

    # greedy algorithm for 0-1 knapsack is not always correct because it doesn't consider all the possibilities
    

maxProfit(p,w,c)

# Brute Force TC O(2^n)
def maxProfitBruteForce(p,w,c):
    return dfs(0,p,w,c)

def dfs(i,p,w,c):
    # if we have reached the end of the list
    if i==len(p):
        return 0
    
    # skip item i
    maxProfit=dfs(i+1,p,w,c)

    # Include item i
    newCapacity=c-w[i]
    if newCapacity>=0:
        profit=p[i]+dfs(i+1,p,w,newCapacity)
        maxProfit=max(maxProfit,profit)

    return maxProfit

print(maxProfitBruteForce(p,w,c))

# Memoization Solution
# Time O(n*c) , Space O(n*c)
# where n is the number of items and c is the capacity

def maxProfitMemoization(p,w,c):
    n,m=len(p),c
    cache=[[-1]*(m+1) for _ in range(n)]

    return dfsMemoization(0,p,w,c,cache)

def dfsMemoization(i,p,w,c,cache):
    if i==len(p):
        return 0
    
    if cache[i][c]!=-1:
        return cache[i][c]
    
    # skip item i
    cache[i][c]=dfsMemoization(i+1,p,w,c,cache)

    # Include item i
    newCap=c-w[i]
    if newCap>=0:
        profit=p[i]+dfsMemoization(i+1,p,w,newCap,cache)
        cache[i][c]=max(cache[i][c],profit)

    return cache[i][c]

print(maxProfitMemoization(p,w,c))

# DP Solution(Tabulation)
# Time O(n*c) , Space O(n*c)
# where n is the number of items and c is the capacity

def maxProfitDP(p,w,c):
    n,m=len(p),c

    dp=[[0]*(m+1) for _ in range(n)]

    # fill the first row with zerios because if we have 0 capacity, we can't take any item
    for i in range(n):
        dp[i][0]=0

    for c in range(m+1):
        if w[0]<=c:
            dp[0][c]=p[0]

    for i in range(1,n):
        for cap in range(i,m+1):
            skip=dp[i-1][cap]
            include=0
            if cap-w[i]>=0:
                include=p[i]+dp[i-1][cap-w[i]]
            dp[i][cap]=max(skip,include)

    return dp[n-1][m]

print(maxProfitDP(p,w,c))