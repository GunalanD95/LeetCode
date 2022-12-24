class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        mod = 1000000007

        dp    = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5 
        
        if n <= 3:
            return dp[n]
        
        
        for i in range(4,n+1):
            dp[i] = (dp[i-1] * 2) + dp[i-3]
            dp[i] %= mod

        return dp[n] % mod

        