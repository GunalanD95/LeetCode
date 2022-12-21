import heapq as hq
class Solution:
    def topologicalSorting(self,adj,indegree,min_heap,topo_ans):
        while min_heap:
            cur_node , count = hq.heappop(min_heap)
            
            topo_ans.append(cur_node)
            
            for child in adj[cur_node]:
                indegree[child] -= 1
                
                if indegree[child] == 0:
                    hq.heappush(min_heap, (child , 0) ) 
    
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj       = [[] for _ in range(numCourses)]
        indegree  = [0] * (numCourses)
        min_heap  = []
        
        for idx in range(len(prerequisites)):
            row = prerequisites[idx][0]
            val = prerequisites[idx][1]
            
            adj[row].append(val)
            indegree[val] += 1
            
        print("indegree",indegree)
        for indx in range(len(indegree)):
            count = indegree[indx]
            if count == 0:
                hq.heappush(min_heap, (indx , 0) )      # (node , count)
                
        topo_ans  = []
        
        self.topologicalSorting(adj,indegree,min_heap,topo_ans)
        
        if len(topo_ans) == numCourses:
            return topo_ans[::-1]
        return []
        
        
        
        