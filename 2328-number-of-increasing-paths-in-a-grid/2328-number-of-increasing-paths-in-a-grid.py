class Solution(object):
    def countPaths(self, grid):
        n = len(grid); m = len(grid[0]); con = 10**9 +7; res = 0
        memo = [[None] * m for _ in range (n)]
        def dfs(i, j, prev_value):
            if min(i,j) < 0 or i >= n or j >= m or grid[i][j] <= prev_value: 
                return 0
            if memo[i][j] is not None:
                return memo[i][j]
            else:
                memo[i][j] = (dfs(i-1, j, grid[i][j]) + dfs(i+1, j, grid[i][j]) + dfs(i, j+1, grid[i][j]) + dfs(i, j-1, grid[i][j]) + 1) % con
                return memo[i][j]
        
        for i in range (n):
            for j in range (m):
                res = (dfs(i, j, 0) + res) % con
        
        return res