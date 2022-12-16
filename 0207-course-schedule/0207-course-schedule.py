import heapq as hq
class Solution:
    def Config(self,arr,N,adj,indegree,min_heap):
        for idx in range(len(arr)):
            row = arr[idx][0]
            val = arr[idx][1]
            adj[row].append(val)
            indegree[val] += 1
        for indx in range(len(indegree)):
            count = indegree[indx]
            if count == 0:
                hq.heappush(min_heap, (count,indx))
        return adj , indegree , min_heap  

    def topologicalSort(self,arr,N,topo_ans):
        adj         = [[] for _ in range(N)]
        indegree    = [0] * (N)
        min_heap    = []

        self.Config(arr,N ,adj , indegree , min_heap)

        while min_heap:
            count , cur_node = hq.heappop(min_heap)
            topo_ans.append(cur_node)
            
            for child in adj[cur_node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    hq.heappush(min_heap, (0,child))
                    
        return topo_ans 
    
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        topo_ans = []
        self.topologicalSort(prerequisites,numCourses,topo_ans)
        print("topo_ans",topo_ans)
        if len(topo_ans) != numCourses:
            return False
        return True  
        
        