#User function Template for python3

from typing import List
from collections import deque 

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        N , M = len(grid) , len(grid[0])
        
        q = deque()
        q.append((source[0],source[1],0)) # (Src,Node, Distance)
        visited        = [[False] * M for _ in range(N)]
        
        visited[source[0]] [source[1]] = True 
        
        directions     = [[0,1],[1,0],[0,-1],[-1,0]]

        while q:
            row , col , distance =  q.popleft()

            if row == destination[0] and col == destination[1]:
                return distance

            
            for i , j in directions:
                cr = row + i
                cc = col + j 
                
                if cr < 0 or cr >= N or cc < 0 or  cc >= M or grid[cr][cc] == 0 or visited[cr][cc]:
                    continue 
                
                visited[cr][cc] = True 
                q.append((cr,cc,distance+1))
                
                
                
                
                
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends