import heapq as hq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        hq.heapify(nums) 
        
        while k != 0:
            value = hq.heappop(nums)
            print("value",value)
            hq.heappush(nums, -value)
            k -= 1
            
        return sum(nums)