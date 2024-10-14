import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def move(h1, h2):
            x, i = heapq.heappop(h1)
            heapq.heappush(h2, (-x, i))

        def get_med(h1, h2, k):
            return h1[0][0] * 1. if k & 1 else (h1[0][0] - h2[0][0]) / 2.

        small, large = [], []
        result = []

        for i, x in enumerate(nums[:k]): 
            heapq.heappush(small, (-x, i))
        
        for _ in range(k - k//2):
            move(small, large)

        result.append(get_med(large, small, k))

        for i, x in enumerate(nums[k:]):
            if x >= large[0][0]:
                heapq.heappush(large, (x, i+k))
                if nums[i] <= large[0][0]:
                    move(large, small)
            else:
                heapq.heappush(small, (-x, i+k))
                if nums[i] >= large[0][0]:
                    move(small, large)
            
            while small and small[0][1] <= i:
                heapq.heappop(small)
            while large and large[0][1] <= i:
                heapq.heappop(large)
            
            result.append(get_med(large, small, k))

        return result