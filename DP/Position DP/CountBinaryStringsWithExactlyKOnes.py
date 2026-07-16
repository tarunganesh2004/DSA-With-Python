# Count Binary Strings with exactly K ones

N=3
k=2

# recursion
def bruteForce(n,k):

    def dfs(i,ones_count):
        if i==n:
            if k==ones_count:
                return 