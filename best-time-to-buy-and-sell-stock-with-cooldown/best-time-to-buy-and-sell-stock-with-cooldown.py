class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N  = len(prices)
        
        @cache
        def find_max_profit(indx,holdings):
            if indx >= N :
                return 0
            
            # two cases
            # if have holding we can sell
            # if not we can buy
            do_nothing  = find_max_profit(indx+1,holdings)
            do_something = 0
            if holdings:
                # we cant buy new one but can we sell or not sell
                do_something =  prices[indx] + find_max_profit(indx+2,0) 
            else:
                do_something  = -prices[indx] + find_max_profit(indx+1,1)
            
            return max(do_nothing,do_something)
        
        
        return find_max_profit(0,0)