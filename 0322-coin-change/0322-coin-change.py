class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        
        dp = [[float('inf')]*(amount+1) for i in range(N+1)]
              
        
        def knapSack(indx,amount_used):
            if indx < 0 or amount_used < 0:
                return 1e5
              
            if amount_used == 0:
                return 0
            
            if dp[indx][amount_used] != float('inf'):
                return dp[indx][amount_used] 
            
            
            dont_take = knapSack(indx - 1,amount_used)
            take_it   = 1e5
            
            if coins[indx] <= amount_used:
                take_it = knapSack(indx,amount_used - coins[indx])
                
                
            dp[indx][amount_used] = min(dont_take, 1 + take_it)
            
            return dp[indx][amount_used] 
        
        
        ans = knapSack(N - 1 ,amount )
        
        if ans != 1e5:
            return ans
        return -1
        