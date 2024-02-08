from functools import lru_cache
class Solution:    
    def dpSquare(self,num,dp):
        if dp[num] != -1:
            return dp[num]
        i = 1
        count = float('inf')
        while i * i <= num:
            dpCount = self.dpSquare(num - (i*i),dp)
            count   = min(count,dpCount + 1)
            i += 1
        dp[num]   = count
        return count 
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        return self.dpSquare(n,dp)
        
        
                
            
            