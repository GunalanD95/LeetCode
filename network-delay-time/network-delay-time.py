from collections import defaultdict
import heapq as hq

class Solution:
    def djk(self,min_heap,graph,distance_arr):
        while min_heap:
            cur_node , cur_dis = hq.heappop(min_heap)
            
            for child,chid_dis in graph[cur_node]:
                if cur_dis + chid_dis < distance_arr[child]:
                    distance_arr[child] = cur_dis + chid_dis
                    hq.heappush(min_heap,(child,distance_arr[child]))
        
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
            
        distance_arr = [float('inf')] * (n+1)
        distance_arr[k] = 0
        
        min_heap     = []
        hq.heappush(min_heap,(k,0)) # ( node, cur_distance )
        
        self.djk(min_heap,graph,distance_arr)
        for node in range(1,n+1):
            if distance_arr[node] == float('inf'):
                return -1
        return max(distance_arr[1:])