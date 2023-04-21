class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def dp(i, curr, remain):
            if i == len(profit):
                return curr == minProfit
            result = 0
            if remain >= group[i]:
                result += dp(i + 1, min(curr + profit[i], minProfit), remain - group[i]) 
            return (result + dp(i + 1, curr, remain)) % mod
        return dp(0, 0, n)        