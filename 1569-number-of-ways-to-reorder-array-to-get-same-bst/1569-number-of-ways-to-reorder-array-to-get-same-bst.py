class Solution:
    def numOfWays(self, A):
        n = len(A)
        mod = 10 ** 9 + 7
        def dfs(i, l, h):
            if h == l + 1: return 1
            if l < A[i] < h:
                return (dfs(i + 1, l, A[i]) * dfs(i + 1, A[i], h) * math.comb(h - l - 2, A[i] - l - 1)) % mod
            return dfs(i + 1, l, h)
        return dfs(0, 0, n + 1) - 1