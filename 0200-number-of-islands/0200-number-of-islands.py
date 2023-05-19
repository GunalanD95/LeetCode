from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        
        def bfs(row, col):
            queue = deque([(row, col)])
            visited[row][col] = True
            
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and not visited[nr][nc]:
                        queue.append((nr, nc))
                        visited[nr][nc] = True
        
        visited = [[False] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    bfs(i, j)
        
        return count
