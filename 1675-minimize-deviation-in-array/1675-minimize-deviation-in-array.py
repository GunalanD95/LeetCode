from collections import deque 
import  heapq as hq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        N = len(nums)
        
        
        ourHeap = []
        min_val = float('inf')
        
        for num in nums:
            if num % 2 == 0:
                hq.heappush(ourHeap, -num)
                min_val = min(num, min_val)
            else:
                hq.heappush(ourHeap, -num * 2)
                min_val = min(num * 2, min_val)
        
        ans = float('inf')
        while ourHeap and ourHeap[0] % 2 == 0:
            max_val = -hq.heappop(ourHeap)
            ans     = min(ans, max_val - min_val)
            new_even = max_val //2
            hq.heappush(ourHeap,-new_even)
            min_val = min(new_even, min_val)
        
        if ourHeap:
            ans = min(-ourHeap[0] - min_val,ans)
            
        return ans
                
            