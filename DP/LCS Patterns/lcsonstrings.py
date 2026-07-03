# Longest common subsequence (2 Strings)
s1="abcabc"
s2="abcd"

# recursion 
def recursion(s1,s2):
    n1,n2=len(s1),len(s2)
    def f(i,j):
        if i==n1 or j==n2:
            return 0
        if s1[i]==s2[j]:
            return 1+f(i+1,j+1)
        return max(f(i+1,j),f(i,j+1))
    return f(0,0)

# tabulation
def tabulation(s1,s2):
    n1,n2=len(s1),len(s2)
    dp=[[0]*(n2+1) for _ in range(n1+1)]
    for i in range(n1-1,-1,-1):
        for j in range(n2-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])
    return dp[0][0]

print(recursion(s1,s2))
print(tabulation(s1,s2))