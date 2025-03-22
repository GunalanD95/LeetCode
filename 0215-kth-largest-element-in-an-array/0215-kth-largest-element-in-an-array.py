import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)
        max_heap = []
        for num in nums:
            if not max_heap or len(max_heap) < k:
                hq.heappush(max_heap,num)
            else:
                top_val = max_heap[0]
                if top_val < num:
                    hq.heappop(max_heap)
                    hq.heappush(max_heap,num)
        return max_heap[0]
