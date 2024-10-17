from collections import defaultdict
import heapq as hq

class Solution:
    def Dijsktra(self,graph,min_heap,dist):
        while min_heap:
            cur_node , time_taken = hq.heappop(min_heap)
            for child,next_time in graph[cur_node]:
                if time_taken + next_time < dist[child]:
                    dist[child] = time_taken + next_time
                    hq.heappush(min_heap,(child,dist[child]))



    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # create a graph
        for src,des,time in times:
            graph[src].append((des,time))

        # create a distance array
        distance_array = [float('inf')] * (n+1)
        distance_array[k] = 0

        # push source node to heap
        min_heap = []
        hq.heappush(min_heap,(k,0)) # (src_node,time_taken)  

        self.Dijsktra(graph,min_heap,distance_array)

        for node in range(1,n+1):
            print(node,distance_array)
            if distance_array[node] == float('inf'):
                return -1

        return max(distance_array[1:])