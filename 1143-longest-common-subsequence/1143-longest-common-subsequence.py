class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n , m = len(text1) , len(text2)
        
        dp = [[-1] * (m+1) for i in range(n+1)]
        
        def DPRecursion(indx1,indx2):
            if indx1 < 0 or indx2 < 0:
                return 0
            
            if dp[indx1][indx2] != -1:
                return dp[indx1][indx2]
            
            if text1[indx1] == text2[indx2]:
                dp[indx1][indx2] =  1 + DPRecursion(indx1-1,indx2-1)
            
            else:
                dp[indx1][indx2] = max(DPRecursion(indx1-1,indx2) , DPRecursion(indx1,indx2-1))
                
                
            return dp[indx1][indx2]
            
            
            
        return DPRecursion(n-1,m-1)
        