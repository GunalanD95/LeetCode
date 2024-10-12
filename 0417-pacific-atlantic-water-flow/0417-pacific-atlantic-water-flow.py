from collections import deque

class Solution:
    def bfs(self, visited, q):
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def outofbound(i, j):
            return i < 0 or j < 0 or i >= self.rows or j >= self.cols

        while q:
            cr, cc = q.popleft()
            cur_val = self.heights[cr][cc]
            
            for r, c in directions:
                nr, nc = cr + r, cc + c
                
                # Flow is allowed if the next cell's height is >= current cell
                if outofbound(nr, nc) or (nr, nc) in visited or self.heights[nr][nc] < cur_val:
                    continue
                
                visited.add((nr, nc))
                q.append((nr, nc))

    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        self.rows, self.cols = len(heights), len(heights[0])
        self.heights = heights
        q1 = deque()  # Pacific queue
        q2 = deque()  # Atlantic queue

        visited1 = set()  # Visited cells for Pacific
        visited2 = set()  # Visited cells for Atlantic
        res = []

        # Add cells adjacent to Pacific (top and left edges) and Atlantic (bottom and right edges)
        for row in range(self.rows):
            q1.append((row, 0))  # Pacific: left edge
            q2.append((row, self.cols - 1))  # Atlantic: right edge
            visited1.add((row, 0))  # Mark as visited for Pacific
            visited2.add((row, self.cols - 1))  # Mark as visited for Atlantic

        for col in range(self.cols):
            q1.append((0, col))  # Pacific: top edge
            q2.append((self.rows - 1, col))  # Atlantic: bottom edge
            visited1.add((0, col))  # Mark as visited for Pacific
            visited2.add((self.rows - 1, col))  # Mark as visited for Atlantic

        # Perform BFS for both oceans
        self.bfs(visited1, q1)
        self.bfs(visited2, q2)

        # Add cells that can flow to both oceans
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in visited1 and (row, col) in visited2:
                    res.append([row, col])

        return res
