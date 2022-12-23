class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2 : return 0
                
        n               = len(prices)
        dp_buy          = [0 for _ in range(n)]
        dp_cooldown     = [0 for _ in range(n)]
        dp_sell         = [0 for _ in range(n)]
        
        dp_cooldown[0]  = 0
        dp_buy[0]       = -prices[0]
        dp_sell[0]      = float('-inf')
        max_prev_buy    = dp_buy[0]
        
        for i in range(1, n):
            dp_cooldown[i]  = max( dp_cooldown[i-1], dp_buy[i-1], dp_sell[i-1] )
            dp_buy[i]       = dp_cooldown[i-1] - prices[i]
            dp_sell[i]      = max_prev_buy + prices[i]
            
            max_prev_buy    = max( max_prev_buy, dp_buy[i] )
            
        return max( dp_cooldown[-1], dp_sell[-1] )        