import heapq as hq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        min_cost  = 0
        
        min_heap = []
        
        # start with the first node in points
        hq.heappush(min_heap,(0,points[0][0],points[0][1]))
        
        visited   = set()
        total_edges = N -1
        
        while min_heap and total_edges >= 0:
            cost , x1 , y1= hq.heappop(min_heap)
            # avoid duplicate nodes
            if (x1,y1) in visited:
                continue
            
            min_cost += cost
            visited.add((x1,y1))
            total_edges -= 1
            # add the edges basically everything ( unvisited ones )
            for node in range(N):
                x2,y2 = points[node][0] , points[node][1]
                if (x2,y2) not in visited:
                    mh = abs(abs(x1-x2)+abs(y1-y2))
                    hq.heappush(min_heap,(mh,x2,y2))
                    
        
        
        return min_cost