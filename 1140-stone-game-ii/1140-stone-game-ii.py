class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @cache
        def dp(i, m, p):
            res = 0 if p == 0 or i == n else inf
            acc = 0
            for j in range(i, min(i + 2 * m, n)):
                acc += piles[j]
                w = max(m, j - i + 1)
                if p == 0:
                    res = max(res, dp(j + 1, w, 1) + acc)
                else:
                    res = min(res, dp(j + 1, w, 0))
            return res
        return dp(0, 1, 0)