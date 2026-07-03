# Longest Palindromic Subsequence LC 516

# this can be done using 2 approaches
# 1. doing lcs with two strings, s1,reverse(s1)

# taking a single string and starting at both ends, i=0,j=n-1
# if both ends match then we move,and 2(since 2 characters), and next we go through s[i+1..j-1]
# if characters dont match we have 2cases, either moving i, and moving j to left, so max(f(i+1,j),f(i,j-1))

s="bbbab"
# recursion
def recursion(s):
    n=len(s)
    def f(i,j):
        if i==j:
            return 1
        if i>j:
            return 0 
        
        if s[i]==s[j]:
            return 2+f(i+1,j-1)
        return max(f(i+1,j),f(i,j-1))
    
# tabulation
def tabulation(s):
    n=len(s)
    # i --> n-1 to 0
    # j -> i+1 to n-1
    dp=[[0]*n for _ in range(n)]
    # i==j
    for i in range(n):
        dp[i][i]=1

    for i in range(n-1,-1,-1):
        for j in range(i+1,n):

            if s[i]==s[j]:
                dp[i][j]=2+dp[i+1][j-1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j-1])
    return dp[0][n-1]

print(tabulation(s))