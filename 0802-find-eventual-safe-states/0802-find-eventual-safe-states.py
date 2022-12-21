from collections import deque
import heapq as hq

class Solution:
    def topologicalSorting(self,adj,indegree,min_heap,topo_ans):
        while min_heap:
            cur_node , count = hq.heappop(min_heap)
            print("cur_node",cur_node)
            topo_ans.append(cur_node)
            
            for child in adj[cur_node]:
                indegree[child] -= 1
                print("child",child,indegree[child])
                if indegree[child] == 0:
                    hq.heappush(min_heap, (child , 0) ) 
                    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N          = len(graph)
        min_heap   = []
        indegree   = [0] * (N)
        ans        = []
        adj       = [[] for _ in range(N)]
        
        for indx in range(N):
            if not graph[indx]:
                hq.heappush(min_heap,(indx,0))
            else:
                for val in graph[indx]:
                    adj[val].append(indx)
                    indegree[indx] += 1
                
                    
        print("ADJ",adj)
        print("indegree",indegree,"min_heap",min_heap)
        self.topologicalSorting(adj,indegree,min_heap,ans)
        print("min_heap",min_heap,"ans",ans,"indegree",indegree)
        
        return sorted(ans)
                    

        
        
        
        
        
        
        
                