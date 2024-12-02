class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        cur_stock = prices[0]
        for stock in prices[1:]:
            if cur_stock < stock:
                profit = max(profit,stock-cur_stock)
            else:
                cur_stock = stock
        

        return profit
        