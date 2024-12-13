from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid) , len(grid[0])
        
        total_oranges_left = 0
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    total_oranges_left += 1
                    
        total_time = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        
        while q and total_oranges_left > 0:
            for _ in range(len(q)):
                cr,cc = q.popleft()
                visited.add((cr,cc))
                for r,c in directions:
                    nr,nc = cr+r,cc+c
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] != 1:
                        continue
                    if (nr,nc) in visited:
                        continue 
                    q.append((nr,nc))
                    total_oranges_left -= 1
                    grid[nr][nc] = 2
            total_time += 1
        return -1 if total_oranges_left != 0 else total_time
        