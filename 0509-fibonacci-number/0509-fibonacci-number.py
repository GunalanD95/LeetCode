class Solution:
    def findFib(self,n,dp):
        if n <= 1:
            return n
        # check value is calculated or not
        if dp[n] == -1:
            dp[n] = self.findFib(n-1,dp) + self.findFib(n-2,dp)
        return dp[n]
        
        
    def fib(self, n: int) -> int:
        # create  a dp array of size n+1
        dp = [-1] * (n+1)
        return self.findFib(n,dp)
        