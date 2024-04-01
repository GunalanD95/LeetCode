import heapq as hq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        N = len(nums)

        max_heap = []

        for num in nums:
            hq.heappush(max_heap,-int(num))

        while max_heap and k > 0:
            val = hq.heappop(max_heap) * -1
            k -= 1

        return str(val)