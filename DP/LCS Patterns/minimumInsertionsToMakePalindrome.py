# Minimum Insertions to Make Palindrome LC 1312(Hard)

s="zzazz"
""" 
we have learnt for two string problems, when ever if the qsn contains 
Convert A → B
Delete operations
Shortest Common Supersequence
Minimum Insertions + Deletions
then --> think of lcs 
if the qsn contains one string+ palindrome
Longest Palindromic Subsequence
Minimum Insertions to Make Palindrome
Minimum Deletions to Make Palindrome
⇒ Think

LPS = LCS(s, reverse(s))
"""

def minInsertions(s):
    n=len(s)
    def lcs(s1,s2):
        n1, n2 = len(s1), len(s2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
    lps=lcs(s,s[::-1])
    return n-lps 

print(minInsertions(s))
s1="leetcode"
print(minInsertions(s1))

# minimum deletions is also same n-lps