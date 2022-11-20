class Solution:
    def climbStairs(self, A: int) -> int:
        # bottom up approach
        A = A+1
        dp = [None] * (A+1)
        dp[0] , dp[1] = 0 , 1

        for i in range(2,A+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[A]        