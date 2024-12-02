class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m , n = len(obstacleGrid) , len(obstacleGrid[0])
        
        @cache
        def find_all_valid_paths(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or obstacleGrid[i][j] == 1:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            down  = find_all_valid_paths(i+1,j)
            right = find_all_valid_paths(i,j+1)
            return down + right
            
        
        return find_all_valid_paths(0,0)        