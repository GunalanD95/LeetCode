from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def out_of_bound(i, j):
            return i < 0 or j < 0 or i >= rows or j >= cols

        def dfs(r, c):
            if out_of_bound(r, c) or grid[r][c] <= 0:
                return 0
            
            # Collect the fish count at this cell
            fish_count = grid[r][c]
            # Mark the cell as visited by setting it to 0
            grid[r][c] = 0
            
            # Explore all four directions
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                fish_count += dfs(r + dr, c + dc)
            
            return fish_count
        
        max_sum = 0
        
        # Start DFS from each cell with fish
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:
                    max_sum = max(max_sum, dfs(row, col))
        
        return max_sum
