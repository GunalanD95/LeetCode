class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        
        dp = [[-1]* (amount+1) for i in range(N+1)]
        
        
        def knapSackCoin(indx, coins_used):
            if indx < 0 or coins_used < 0:
                return 0
            
            
            if coins_used == 0:
                return 1
            
            if dp[indx][coins_used] != -1:
                return dp[indx][coins_used]
            
            take_it  = 0

            if coins[indx] > coins_used:
                dont_take = knapSackCoin( indx-1, coins_used )
            else:
                dont_take = knapSackCoin( indx-1, coins_used )
                
                take_it   = knapSackCoin( indx,   coins_used - coins[indx])
                
                
            dp[indx][coins_used] = dont_take + take_it

            return dp[indx][coins_used]

        return knapSackCoin(N-1, amount)