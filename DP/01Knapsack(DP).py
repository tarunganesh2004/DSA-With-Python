p = [5, 6, 2]
w = [3, 4, 1]
cap = 6

# Top down approach
def knapDp(p,w,cap):
    n=len(p)
    dp = [[0] * (cap + 1) for _ in range(n+ 1)]

    for i in range(1,n+1):
        for j in range(1,cap+1):
            if w[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],p[i-1]+dp[i-1][j-w[i-1]])
            else:
                # exclude
                dp[i][j]=dp[i-1][j]

    return dp[n][cap],dp

result, dp_table = knapDp(p, w, cap)
print("Maximum Profit:", result)
print("DP Table:")
for row in dp_table:
    print(row)