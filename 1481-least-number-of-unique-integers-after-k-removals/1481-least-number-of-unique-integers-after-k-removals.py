from collections import Counter
import heapq as hq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        amap = Counter(arr)
        
        min_heap = []
        
        for key,value in amap.items():
            hq.heappush(min_heap,(value,key))
            
        
        while min_heap and k > 0:
            count , num = hq.heappop(min_heap)
            if count > 1:
                hq.heappush(min_heap,(count-1,num))
            k -= 1
        return len(min_heap)