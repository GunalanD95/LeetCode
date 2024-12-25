from collections import defaultdict
import heapq as hq
class Solution:
    def findOrder(self, n: int, courses: List[List[int]]) -> List[int]:
        indeg = [0] * n
        graph = defaultdict(list)
        
        for u,v in courses:
            graph[v].append(u)
            indeg[u] += 1
            
        min_heap = []
        for node,count in enumerate(indeg):
            if count == 0:
                hq.heappush(min_heap,node)
                
                
        ans = []
        
        
        while min_heap:
            cur_node = hq.heappop(min_heap)
            ans.append(cur_node)
            
            for course in graph[cur_node]:
                indeg[course] -= 1
                if indeg[course] == 0:
                    hq.heappush(min_heap,course)
        if len(ans) != n: return []
        return ans