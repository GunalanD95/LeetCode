import heapq as hq

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_heap = []
        
        for num in happiness:
            hq.heappush(max_heap,-num)
        
        
        total = 0
        counter = 0
        
        while k > 0 and happiness:
            cur_val = -hq.heappop(max_heap)
            cur_val -= counter
            
            if cur_val < 0:
                break
            
            total  += cur_val
            
            counter += 1
            k -= 1
        
        return total 