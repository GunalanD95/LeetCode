from collections import deque
import heapq as hq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        N, M = len(heights), len(heights[0])
        
        # Min-heap to process cells with least effort first
        min_heap = []
        hq.heappush(min_heap, (0, 0, 0))  # (effort, row, col)
        
        # Directions for movement
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        # To track the minimum effort required to reach each cell
        visited = [[float('inf')] * M for _ in range(N)]
        visited[0][0] = 0
        
        while min_heap:
            cur_effort, cr, cc = hq.heappop(min_heap)
            
            # If we reach the bottom-right corner, return the effort
            if cr == N - 1 and cc == M - 1:
                return cur_effort
            
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                
                # Check boundaries
                if 0 <= nr < N and 0 <= nc < M:
                    # Calculate effort for the new cell
                    new_effort = max(cur_effort, abs(heights[cr][cc] - heights[nr][nc]))
                    
                    # Only push to heap if we found a better path to the cell
                    if new_effort < visited[nr][nc]:
                        visited[nr][nc] = new_effort
                        hq.heappush(min_heap, (new_effort, nr, nc))
        
        # Return -1 if somehow no path is found (though not expected in valid inputs)
        return -1
