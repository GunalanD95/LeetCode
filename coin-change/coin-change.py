class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        min_coins = float('inf')
        
        @cache
        def find_all(indx,cur_coins):
            if indx >= N or cur_coins > amount:
                return float('inf')
            
            if cur_coins == amount:
                return 0
            
            # dont take current coind
            dont_take = find_all(indx+1,cur_coins)
        
            # take it
            take_it   = 1 + find_all(indx,cur_coins+coins[indx])
            
            return min(dont_take,take_it)
        
        
        ans = find_all(0,0)
        return -1 if ans == float('inf') else ans
        