class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dp   = [[None] * cols for i in range(rows)]
        
        def getMeMin(row,col,dp):
            if row >= rows or col >= cols:
                return float('inf')
            
            if row == (rows -1 ) and col == (cols -1):
                dp[row][col] = grid[row][col]
                
            if dp[row][col] != None:
                return dp[row][col] 
            
            dp[row][col] = grid[row][col] + min (getMeMin(row+1,col,dp), 
                                                 getMeMin(row,col+1,dp))
		
        
            return dp[row][col]
        
        
        return getMeMin(0,0,dp)
