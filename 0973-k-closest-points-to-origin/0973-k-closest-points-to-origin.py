import math
from collections import defaultdict
import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        min_val = float('inf')
        hashmap = defaultdict(list)
        for point in points:
            x1 , y1  = abs(point[0]) , abs(point[1])
            
            sqrt_sum = (x1*x1) + (y1*y1)
            hashmap[sqrt_sum].append(point)
            
            hq.heappush(minHeap,sqrt_sum)
            
            
        ans = []
        
        while k != 0:
            key = hq.heappop(minHeap)
            ans.extend(hashmap[key])
            del hashmap[key]
            k -=1
            
        return ans 
        