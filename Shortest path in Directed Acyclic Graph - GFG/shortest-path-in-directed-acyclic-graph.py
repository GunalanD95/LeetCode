#User function Template for python3

from typing import List
from collections import deque
import heapq as hq

class Solution:
    def djikstra(self,adj,min_heap,distance):
        
        while min_heap:
            parent_node , parent_distance = hq.heappop(min_heap)
            
            for child_node , child_distance in adj[parent_node]:
                if parent_distance + child_distance < distance[child_node]:
                    newDistance     = parent_distance + child_distance
                    distance[child_node] = newDistance
                    hq.heappush(min_heap , (child_node,newDistance))
            
    
    
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        adj      = [[] for _ in range(n)]
        
        for idx in range(len(edges)):
            row = edges[idx][0]
            val = edges[idx][1]
            weg = edges[idx][2]
            adj[row].append((val,weg))  # (node,dist)
            
        distance     = [float('inf')] * (n)
        distance[0]  = 0
        
        min_heap     = []
        hq.heappush(min_heap , (0,0))   # (node,dist)
        
        self.djikstra(adj,min_heap,distance)
        
        for node in range(n):
            if distance[node] == float('inf'):
                distance[node] = -1 
                
        
        return distance
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends