from collections import deque , defaultdict
import heapq as hq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
    
        for u,v,w in flights:
            graph[u].append((v,w))
            
        distance_arr = [float('inf')] * n
        distance_arr[src] = 0
        min_heap = []
        hq.heappush(min_heap,(0,src,0)) # (source , fare)
        
        while min_heap:
            stops ,cur_node , cur_dis = hq.heappop(min_heap)
            
            if stops > k:
                continue
            
            for child,chid_dis in graph[cur_node]:
                if cur_dis + chid_dis < distance_arr[child]:
                    distance_arr[child] = cur_dis + chid_dis
                    hq.heappush(min_heap,(stops+1,child,distance_arr[child]))
        
        return distance_arr[dst] if distance_arr[dst] != float('inf') else -1