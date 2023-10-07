from functools import lru_cache

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        @lru_cache(None)
        def dp(arr_len, lrg_num, search_cost):
            if arr_len == 1:
                return 1 if search_cost == 1 else 0
            if search_cost == 0: # optional
                return 0
            
            # no searchcost happens on last number
            ans = dp(arr_len - 1, lrg_num, search_cost) * lrg_num
            
            # searchcost happens on last number
            ans += sum(dp(arr_len - 1, num, search_cost - 1) for num in range(1, lrg_num))   
                
            return ans % 1000000007
        
        return sum([dp(n, num, k) for num in range(1, m + 1)]) % 1000000007