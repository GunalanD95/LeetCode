class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        
        @cache
        def find_all_valid_paths(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return float('inf')
            
            if i == m-1 and j==n-1:
                return grid[i][j]
            
            
            down  = find_all_valid_paths(i+1,j)
            right = find_all_valid_paths(i,j+1)
            print(grid[i][j],down,right,"i:j",(i,j))
            return grid[i][j] + min(down,right)
            
        
        return find_all_valid_paths(0,0)         