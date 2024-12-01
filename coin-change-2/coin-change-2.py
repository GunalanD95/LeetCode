class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        
        @cache
        def find_ways(indx,cur_coins):
            if indx >= N or cur_coins > amount:
                return 0
            
            if cur_coins == amount:
                return 1
            
            # dont take cur_coin
            dont_take = find_ways(indx+1,cur_coins)
            
            # take cur_coin
            take_it   = find_ways(indx,cur_coins + coins[indx])
            
            return dont_take + take_it
        
        
        return find_ways(0,0)