import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        if N == 1: return nums[0]
        
        
        max_sum = -sys.maxsize - 1
        cur_sum = -sys.maxsize - 1
        for i in nums:
            cur_sum += i
            if i > cur_sum:
                cur_sum = i
                
            max_sum = max(max_sum,cur_sum)
        return max_sum
        
        