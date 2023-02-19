class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        
        max_profit = 0
        cur_stock  = prices[-1]
        
        for i in range(N-2,-1,-1):
            if prices[i] > cur_stock:
                cur_stock = prices[i]
            else:
                value = cur_stock - prices[i]
                max_profit = max(value,max_profit)
                
                
        return max_profit
        