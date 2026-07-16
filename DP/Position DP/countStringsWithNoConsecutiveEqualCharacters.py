# Count Strings with no consecutive equal characters
"""
This problem has direct optimized solution
1st position kchoices
every nxt position k-1 choices
total = k*(k-1)*(k-1)*..........*(k-1) -> n-1 times

ans=k*(k-1)^(n-1)
"""

n=3
k=2 # valid : ABA, BAB

# state: (i,prev_char)
def bruteForce(n,k):

    def dfs(i,prev_char):
        if i==n:
            return 1 
        ans=0
        for char in range(k):
            if char!=prev_char:
                ans+=dfs(i+1,char)
        return ans 

    ans=0
    # choose 1st character
    for first_char in range(k):
        ans+=dfs(1,first_char)
    return ans

# memoization
def memoization(n,k):
    memo=[[-1]*k for _ in range(n+1)]
    def dfs(i,prev_char):
        if i==n:
            return 1

        if memo[i][prev_char]!=-1:
            return memo[i][prev_char]

        ans=0
        for char in range(k):
            if char!=prev_char:
                ans+=dfs(i+1,char)

        memo[i][prev_char]=ans 
        return ans 
    ans=0
    for first_char in range(k):
        ans+=dfs(1,first_char)
    return ans 


# tabulation
def tabulation(n, k):
    dp = [[0] * k for _ in range(n + 1)]
    # Base case
    for prev_char in range(k):
        dp[n][prev_char] = 1

    # Fill backwards
    for i in range(n - 1, 0, -1):
        for prev_char in range(k):
            ans = 0
            for char in range(k):
                if char != prev_char:
                    ans += dp[i + 1][char]
            dp[i][prev_char] = ans

    # Choose first character separately
    ans = 0

    for first_char in range(k):
        ans += dp[1][first_char]

    return ans

# optimized direct math formula
def optimized(n,k):
    if n==0:
        return 0
    
    return k*(k-1)**(n-1)

print(bruteForce(n,k))
