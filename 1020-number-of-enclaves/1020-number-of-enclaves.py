from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        N , M = len(grid) , len(grid[0])
        
        q = deque()
        # moves = 0
        ones  = 0
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    ones += 1
                # appending all 1's from the border
                if i == 0 or j == 0 or i == N-1 or j == M-1:
                    if grid[i][j] == 1:
                        q.append( (i,j) )
                        visited[i][j] = True 
                        ones -= 1
                        
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        while q:
            row , col = q.popleft()
            
            for i , j in directions:
                cr = row + i
                cc = col + j
                
                if cr < 0 or cr >= N or cc < 0 or cc >= M or visited[cr][cc] or grid[cr][cc] == 0:
                    continue
                    
                visited[cr][cc] = True
                q.append( (cr,cc) )
                ones -= 1
                
        return ones
                
                        
            
                        
        
                        
        