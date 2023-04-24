import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        '''insert into max_heap '''
        max_heap = []
        for num in stones:
            hq.heappush(max_heap,-num)
            
            
        
        while max_heap:
            max_val1 = - (hq.heappop(max_heap))
            if not max_heap:
                return max_val1
            max_val2 = - (hq.heappop(max_heap))
            
            if max_val1 == max_val2:
                continue
                
                
            new_val  =  max_val1 - max_val2
            hq.heappush(max_heap,-new_val)
            
        return abs(max_heap[0]) if max_heap else 0
            
            
            