from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        
        if grid[0][0] == 1:
            return -1

        def check_out_of_bound(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return True
            return False
        
        q = deque()
        q.append((0,0,0)) # 

        visited = set()
        visited.add((0,0))
        
        directions = [
            [1, 0],   # Down
            [0, 1],   # Right
            [-1, 0],  # Up
            [0, -1],  # Left
            [1, 1],   # Down-Right (Diagonal)
            [1, -1],  # Down-Left (Diagonal)
            [-1, 1],  # Up-Right (Diagonal)
            [-1, -1]  # Up-Left (Diagonal)
        ]
        
        while q:
            cr,cc,cl =  q.popleft()
            
            if cr == rows-1 and cc == cols-1:
                return cl+1
            

            for r,c in directions:
                nr,nc = r+cr , c+cc
                
                if check_out_of_bound(nr,nc) or (nr,nc) in visited or grid[nr][nc] == 1:
                    continue
                    
                visited.add((nr,nc))
                q.append((nr,nc,cl+1))
        
        
        return -1
        
        