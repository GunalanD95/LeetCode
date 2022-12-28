import heapq as hq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total_sum  = sum(piles)
        max_heap = []
        for i in piles:
            x = -i
            hq.heappush(max_heap,x)

        while max_heap and k:
            value = -(hq.heappop(max_heap))
            if value & 1:
                floor = math.ceil(value//2) + 1
            else:
                floor = math.ceil(value//2)
            total_sum -= floor
            hq.heappush(max_heap , -floor)
            k -=1

        # print("-sum(max_heap)",-sum(max_heap))
        return -sum(max_heap)