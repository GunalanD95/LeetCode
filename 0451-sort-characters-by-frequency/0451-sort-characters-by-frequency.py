from collections import Counter
import heapq as hq
class Solution:
    def frequencySort(self, s: str) -> str:
        CounterMap = Counter(s)
        max_heap = []
        for i in CounterMap:
            hq.heappush(max_heap, (-CounterMap[i] , i) )
            
        ans = ''
        while max_heap:
            val , char = hq.heappop(max_heap)
            val = (val) * -1
            while val != 0:
                ans = ans + char
                val -= 1
                
                
        return ans 