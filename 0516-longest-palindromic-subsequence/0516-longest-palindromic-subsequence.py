class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)  
        dp = [[-1] * (N+1) for _ in range(N+1)]
        def DP(indx1,indx2):
            if indx1 >= N or indx2 < 0:
                return 0
            
            if dp[indx1][indx2] != -1:
                return dp[indx1][indx2]
            
            
            if s[indx1] == s[indx2]:
                dp[indx1][indx2] = DP(indx1+1,indx2-1) + 1
                
            else:
                dp[indx1][indx2] = max (
                                       DP(indx1+1,indx2) ,
                                       DP(indx1,indx2-1) 
                )
            return dp[indx1][indx2]

        return DP(0,N-1)