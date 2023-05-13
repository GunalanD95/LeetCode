class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        MOD = 10** 9 + 7
        
        @cache
        def count(length):
            if length > high:
                return 0
            
            res = 1 if length >= low else 0
            
            res += count(length + zero) + count(length + one)
            
            
            return res % MOD
        
        
        
        
        return count(0)
        