class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        cols = len(triangle[rows - 1])
        
        # create dp - matrix
        dp = [[-1] * len(triangle[i]) for i in range(rows)]
        
        # Mincost(i,j) = mat[i][j] + min( Mincost(i-1,j)  , Mincost(i-1,j+1) )
        
        
        # BOTTOM UP APPROACH 

        def triaSum(row,col,dp,triangle):
            
            # base cases
            if row >= rows or col >= cols:
                return 0
            
            if row == rows -1:
                dp[row][col] = triangle[row][col]

            if dp[row][col] != -1:
                return dp[row][col]

            dp[row][col] = triangle[row][col] + min(triaSum(row+1,col,dp,triangle),
                                                    triaSum(row+1,col+1,dp,triangle))

            return dp[row][col] 
        
        triaSum(0,0,dp,triangle)
        return dp[0][0]