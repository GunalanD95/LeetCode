from collections import deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        island_id = 2  # Start from 2 to differentiate from original 1s
        island_sizes = {0: 0}  # Mapping island ID -> size
        
        # Step 1: Find all islands and assign unique IDs
        def bfs(r, c, island_id):
            q = deque([(r, c)])
            grid[r][c] = island_id
            size = 1
            while q:
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = island_id
                        q.append((nr, nc))
                        size += 1
            return size
        
        # Assign unique IDs to islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_sizes[island_id] = bfs(r, c, island_id)
                    island_id += 1
        
        # Step 2: Try flipping each `0` to `1`
        max_island = max(island_sizes.values())  # Default max island if no `0` exists
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen_islands = set()
                    new_size = 1  # Start with the flipped cell
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 1:
                            seen_islands.add(grid[nr][nc])  # Unique islands
                    new_size += sum(island_sizes[iid] for iid in seen_islands)
                    max_island = max(max_island, new_size)

        return max_island
