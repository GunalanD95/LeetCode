class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        
        dp = [[-1]*(m) for i in range(n)]
        
        def backtracking(i,j):
            # base case - we reached end of t --> found combination so return 1
            if j >= m:
                return 1
            
            # if j is still left , but we have exhausted i means we have no options return 0
            if i >= n :
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] =  backtracking(i+1,j) + backtracking(i+1,j+1)
            else:
                dp[i][j] =  backtracking(i+1,j)
                
            return dp[i][j]
                
        
        
        backtracking(0,0)
        return dp[0][0]
        