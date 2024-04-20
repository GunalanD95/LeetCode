class Solution:
    def bfs(self, row, col):
        q = deque()
        q.append((row,col))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        end_row, end_col = row,col
        self.visited.add((row,col))
        while q:
            cr, cc = q.popleft()                        
            end_row, end_col = cr,cc
            
            for r, c in directions:
                nr, nc = cr + r, cc + c
                if (
                    0 <= nr < self.rows
                    and 0 <= nc < self.cols
                    and self.grid[nr][nc] == 1
                    and (nr, nc) not in self.visited
                ):
                    q.append((nr, nc))
                    self.visited.add((nr, nc))
                    
                    
        return end_row, end_col
                    
                    
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        if not land or not land[0]:
            return 0
        
        self.rows, self.cols = len(land), len(land[0])
        self.visited = set()
        self.grid = land

        total_islands = []

        for row in range(self.rows):
            for col in range(self.cols):
                if land[row][col] == 1 and (row, col) not in self.visited:
                    cur = [row,col]
                    end_row,end_col = self.bfs(row, col)
                                        
                    cur.append(end_row)
                    cur.append(end_col)
                    
                    total_islands.append(cur)
                    
        return total_islands
        