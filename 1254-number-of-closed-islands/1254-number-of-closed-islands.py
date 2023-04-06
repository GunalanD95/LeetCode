from collections import deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        count = 0
        
        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))
            is_closed = True
            
            while queue:
                cur_row, cur_col = queue.popleft()
                if cur_row == 0 or cur_col == 0 or cur_row == rows-1 or cur_col == cols-1:
                    is_closed = False
                
                for r, c in directions:
                    new_row, new_col = cur_row+r, cur_col+c
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or (new_row, new_col) in visited or grid[new_row][new_col] == 1:
                        continue
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
            
            return is_closed
        
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and (row, col) not in visited:
                    is_closed = bfs(row, col)
                    if is_closed:
                        count += 1
        
        return count
