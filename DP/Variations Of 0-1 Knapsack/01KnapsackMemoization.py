p = [5, 6, 2]
w = [3, 4, 1]
cap = 6


def knapMemoization(p, w, cap, n, mem=None):
    # problems extra space and stack overflow

    # Initialize memo table
    if mem is None:
        mem = [[-1] * (cap + 1) for _ in range(n + 1)]

    # base case
    if n == 0 or cap == 0:
        return 0

    # check if already computed
    if mem[n][cap] != -1:
        return mem[n][cap]

    # exclude
    if w[n - 1] > cap:
        # skip
        mem[n][cap] = knapMemoization(p, w, cap, n - 1, mem)

    else:
        mem[n][cap] = max(
            knapMemoization(p, w, cap, n - 1, mem),
            p[n - 1] + knapMemoization(p, w, cap - w[n - 1], n - 1, mem),
        )

    return mem[n][cap] # O(n*capacity)


print(knapMemoization(p, w, cap, len(p)))
