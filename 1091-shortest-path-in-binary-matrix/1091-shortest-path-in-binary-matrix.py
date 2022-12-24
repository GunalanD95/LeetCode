from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N , M = len(grid) , len(grid[0])
        
        if grid[0][0] == 1:
            return - 1
        q = deque()
        q.append((0,0,1)) # (Src,Node, Distance)
        visited        = [[False] * M for _ in range(N)]
        
        visited[0] [0] = True 
        
        directions     = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        while q:
            row , col , distance =  q.popleft()

            print(row,col,distance)
            if row == N- 1 and col == M -1:
                return distance

            
            for i , j in directions:
                cr = row + i
                cc = col + j 
                
                if cr < 0 or cr >= N or cc < 0 or  cc >= M or grid[cr][cc] == 1 or visited[cr][cc]:
                    print("noqu",cr,cc)
                    continue 
                
                print("yes",cr,cc)
                visited[cr][cc] = True 
                q.append((cr,cc,distance+1))

        return -1        