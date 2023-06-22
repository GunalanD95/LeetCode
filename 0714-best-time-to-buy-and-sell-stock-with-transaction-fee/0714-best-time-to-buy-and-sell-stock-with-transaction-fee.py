class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @lru_cache(None)
        def canTrade( ind,buy ) :
            if ind >= len(prices) : return 0
            if buy :
                return max(canTrade(ind + 1, buy), canTrade(ind + 1, 1 - buy) - prices[ind])
            else :
                return max(canTrade(ind + 1, buy), 
                    canTrade(ind + 1, 1 - buy) + prices[ind] - fee)
        
        return canTrade(0,1)