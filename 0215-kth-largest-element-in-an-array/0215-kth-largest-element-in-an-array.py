import heapq as hq 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap = []
        for num in nums:
            hq.heappush(max_heap,-num)
        
        
        val = 0
        while max_heap and k !=0:
            val = -1 * hq.heappop(max_heap)
            k -= 1
            
        return val
        