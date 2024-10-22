from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Queue for BFS: (row, col, distance, obstacles eliminated)
        queue = deque([(0, 0, 0, k)])  # Start from (0, 0) with distance 0 and k obstacles
        visited = [[[False] * (k + 1) for _ in range(cols)] for _ in range(rows)]
        visited[0][0][k] = True
        
        while queue:
            r, c, dist, obs_elim = queue.popleft()
            
            # Check if we've reached the bottom-right corner
            if r == rows - 1 and c == cols - 1:
                return dist
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                
                # Check if the new position is within bounds
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    new_obs_elim = obs_elim - grid[new_r][new_c]  # Decrease obstacle count if it's an obstacle
                    
                    # Check if we can proceed to this cell
                    if new_obs_elim >= 0 and not visited[new_r][new_c][new_obs_elim]:
                        visited[new_r][new_c][new_obs_elim] = True
                        queue.append((new_r, new_c, dist + 1, new_obs_elim))
        
        return -1  # If we exit the loop without finding a path