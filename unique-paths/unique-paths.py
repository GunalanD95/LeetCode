class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def find_all_valid_paths(i,j):
            if i < 0 or i > m or j < 0 or j > n:
                return 0
            
            if i == m and j == n:
                return 1
            
            down  = find_all_valid_paths(i+1,j)
            right = find_all_valid_paths(i,j+1)
            return down + right
            
        
        return find_all_valid_paths(1,1)
        