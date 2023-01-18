import math
from collections import defaultdict
import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        N = len(points)
        
        min_heap = []
        
        for i in range(N):
            sqrt = ( points[i][0] * points[i][0] ) + (points[i][1] * points[i][1])
            hq.heappush(min_heap, (sqrt,points[i]))
            
            
        ans = []
        while k > 0:
            val , point = hq.heappop(min_heap)
            ans.append(point)
            k -= 1
            
        return ans
        