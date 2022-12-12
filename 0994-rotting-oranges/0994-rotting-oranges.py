from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        N , M = len(grid) , len(grid[0])
        
        fresh_tom = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    q.append((i,j))
                    
                elif grid[i][j] == 1:
                    fresh_tom += 1
                    
                    
        minutes = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        while q and fresh_tom > 0:
            for i in range(len(q)):
                row , col = q.popleft()
                
                for rd , cd in directions:
                    cr = row + rd
                    cc = col + cd
                    
                    if cr < 0 or cc < 0 or cr >= N or cc >= M or grid[cr][cc] != 1:
                        continue
                        
                    # make it rotten 
                    grid[cr][cc] = 2
                    fresh_tom   -= 1
                    q.append((cr,cc))
                
            minutes += 1
            
            
        return minutes if fresh_tom == 0 else -1
            
        
        
        
        
        