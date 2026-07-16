# Dice Throw (Classic Position + Sum DP) LC 1155
"""
You have N dice, each having faces 1 to 6.

Find the number of ways to obtain a total sum of target.
"""

n=2
target=7

# bruteForce
def bruteForce(n,target):
    def dfs(i,cur_sum):
        if i==n:
            return 1 if cur_sum==target else 0
        
        ans=0
        for face in range(1,7):
            ans+=dfs(i+1,cur_sum+face)
        return ans 
    return dfs(0,0)

def tabulation(n,target):
    dp=[[0]*(target+1) for _ in range(n+1)]
    dp[n][target]=1

    for i in range(n-1,-1,-1):
        for cur_sum in range(target,-1,-1):
            ans=0

            for face in range(1,7):
                if cur_sum+face<=target:
                    ans+=dp[i+1][cur_sum+face]
            dp[i][cur_sum]=ans 
    return dp[0][0]

print(bruteForce(n,target))
print(tabulation(n,target))

"""
This problem can be further extended to leetcode 1155
in this we have n dice, k faces, should sum target
so logic is all same as above
but in for loop we iterate face value upto k+1
for face in range(1,k+1)
"""