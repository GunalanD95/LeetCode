from collections import defaultdict , deque
import heapq as hq

class Solution:    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph =  defaultdict(list)
        
        for u , v , w in flights:
            graph[u].append((v,w))
            
        q = deque()
        q.append((0,src,0))
        
        dist = [float('inf')] * n
        dist[src] = 0
        
        while q:
            stops , node ,fare = q.popleft()
            
            if stops > k:
                continue
                
            
            for child , cost in graph[node]:
                if cost + fare < dist[child] and stops <= k:
                    dist[child] = cost + fare
                    q.append((stops + 1, child, cost + fare ))
        
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
        
        