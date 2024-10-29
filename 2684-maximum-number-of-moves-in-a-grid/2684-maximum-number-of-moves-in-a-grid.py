class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        
        
        max_moves = 0
        
        @cache
        def dfs(i,j,prev):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 0
            
            if grid[i][j] <= prev:
                return 0
            
            cur   = grid[i][j]
            one   = dfs(i-1,j+1,cur)
            two   = dfs(i,j+1,cur)
            three = dfs(i+1,j+1,cur)
            
            
            return 1 + max(one,two,three)
            
        
        for row in range(rows):
            cur_moves = dfs(row,0,float('-inf')) -1
            max_moves = max(max_moves,cur_moves)
        
        
        return max_moves