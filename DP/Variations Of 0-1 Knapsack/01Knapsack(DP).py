wt = [1, 3, 4]
profits = [15, 20, 30]
W = 4 # capacity


def knapsack(wt, val, W):
    n = len(wt)

    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # here dp[i][j]=maximum profit using items from i onwards with capacity j
    # ans=dp[0][W]
    for i in range(n - 1, -1, -1):  # bottom up
        for cap in range(W + 1):
            not_take = dp[i + 1][cap]
            take = 0
            if wt[i] <= cap:
                take = val[i] + dp[i + 1][cap - wt[i]]

            dp[i][cap] = max(take, not_take)

    return dp[0][W],dp


# we can define state in other way also
# maximize profit using 1st i items with capacity j
def knapsack1(wt, val, W):  # top down
    n = len(wt)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # here dp[i][j]=maximum profit using first  i items with capacity j
    # ans=dp[n][W]
    for i in range(1, n + 1):
        for cap in range(1, W + 1):
            not_take = dp[i - 1][cap]
            take = 0
            if wt[i - 1] <= cap:
                take = val[i - 1] + dp[i - 1][cap - wt[i - 1]]

            dp[i][cap] = max(take, not_take)

    return dp[n][cap],dp


result, dp_table = knapsack(wt,profits,W)
print("Maximum Profit:", result)
print("DP Table:")
for row in dp_table:
    print(row)
