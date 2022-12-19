from collections import defaultdict , deque 
import heapq as hq

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        distance_array    = [float('inf')] * V
        distance_array[S] = 0                  # src to src distance is zero 
        min_heap          = []
        
        hq.heappush(min_heap,(S,0))            # src-node , distance
        
        while min_heap:
            pnode , pnode_distance  = hq.heappop(min_heap)
            
            for child_node , child_dis in adj[pnode]:
                if pnode_distance + child_dis < distance_array[child_node]:
                    distance_array[child_node] = pnode_distance + child_dis
                    hq.heappush(min_heap,(child_node,distance_array[child_node])) 
                    
        return distance_array
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends