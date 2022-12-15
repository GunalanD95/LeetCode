from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        N , M = len(mat) , len(mat[0])
        visited = [[False] * (M) for _ in range(N)]
        
        
        total_ones = 0
        for i in range(N):
            for j in range(M):
                # we are appending all the ones intially in Queue 
                if mat[i][j] == 0:
                    total_ones += 1
                    q.append((i,j,0))  # (row,col,count)
                    visited[i][j] = True 
                    
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        
        while q:
            # for each ones we 
            # print("q",q)
            row , col , count = q.popleft()
            
            for i , j in directions:
                cr = row + i
                cc = col + j

                if cr < 0 or cc < 0 or cr >= N or cc >= M or visited[cr][cc] or mat[cr][cc] != 1 :
                    continue
                    
                mat[cr][cc] = count + 1
                
                q.append((cr,cc,count+1))
                
                visited[cr][cc] = True
                
                
        return mat 
                
            
        
        
        