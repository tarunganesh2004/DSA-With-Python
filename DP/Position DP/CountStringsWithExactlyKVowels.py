# Count Strings with exactly k vowels

n=3
k=2

# brute force
def recursion(n,k):

    def dfs(i,v_c):
        if v_c>k:
            return 0
        if i==n:
            return 1 if v_c==k else 0
        
        ans=0
        # choose a vowel
        ans+=5*dfs(i+1,v_c+1) # since there are 5vowels

        # choose a consonant
        ans+=21*dfs(i+1,v_c)

        return ans 
    return dfs(0,0)

def memoization(n,k):
    memo = [[-1] * (k + 1) for _ in range(n + 1)]
    def dfs(i, v_c):
        if v_c > k:
            return 0

        if i == n:
            return 1 if v_c == k else 0

        if memo[i][v_c] != -1:
            return memo[i][v_c]

        # Choose a vowel
        vowel_ways = 5 * dfs(i + 1, v_c + 1)
        # Choose a consonant
        consonant_ways = 21 * dfs(i + 1, v_c)
        memo[i][v_c] = vowel_ways + consonant_ways
        return memo[i][v_c]
    return dfs(0, 0)

def tabulation(n,k):
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[n][k]=1
    for i in range(n-1,-1,-1):
        for v_c in range(k,-1,-1):
            # choose a vowel
            vowel_ways=0
            if v_c<=k:
                vowel_ways=5*dp[i+1][v_c+1]
            
            # choose a consonant
            consonant_ways=21*dp[i+1][v_c]

            dp[i][v_c]=vowel_ways+consonant_ways
    return dp[0][0]

print(recursion(n,k))
print(tabulation(n,k))
