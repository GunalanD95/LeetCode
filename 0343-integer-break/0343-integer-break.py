class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None , 1]
        
        for m in range(2,n+1):
            i = 1
            j = m-1
            
            max_prod = 0
            
            while i <= j:
                max_prod = max( max_prod, max(i,dp[i]) * max(j,dp[j]) )
                i += 1
                j -= 1
            dp.append(max_prod)
        
        return dp[n]