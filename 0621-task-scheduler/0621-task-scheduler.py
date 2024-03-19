import heapq as hq
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        N = len(tasks)
        if n == 0:
            return N
        
        hmap = defaultdict(list)
        min_heap = []
        
        for idx, task in enumerate(tasks):
            if task not in hmap:
                hmap[task].append(0)
                hq.heappush(min_heap, (0, task))
            else:
                val = hmap[task][-1] 
                hmap[task].append(val + n + 1)
                hq.heappush(min_heap, (val + n + 1, task))
            
        time = 0
        while min_heap:
            idx, task = hq.heappop(min_heap)
            if time < idx:
                time = idx
            time += 1
            
        return time
