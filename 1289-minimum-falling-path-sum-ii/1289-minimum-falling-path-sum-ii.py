class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid) , len(grid[0])

        
        @cache
        def min_sum(row,prev_col):
            if row >= rows:
                return 0 
            
            res = float('inf')
            for col in range(cols):
                if col != prev_col:                    
                    res = min(res , grid[row][col] + min_sum(row+1,col))
            return res
    
        
        return min_sum(0,500)