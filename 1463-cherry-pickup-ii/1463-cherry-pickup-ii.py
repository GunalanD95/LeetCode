class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        direction = [(1,0),(1,-1),(1,1)]
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i1,j1,i2,j2):
            if i1 >= m:
                return 0
            
            if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
                return - float("inf")
            
            res = 0
            
            for di1, dj1 in direction:
                for di2, dj2 in direction:
                    res = max(res, grid[i1][j1] + dfs(i1+di1,j1+dj1,i2+di2,j2+dj2)) if (i1 == i2 and j1 == j2)\
                    else max(res, grid[i1][j1] + grid[i2][j2] + dfs(i1+di1,j1+dj1,i2+di2,j2+dj2))
            
            return res
        
        
        return dfs(0,0,0,n-1)