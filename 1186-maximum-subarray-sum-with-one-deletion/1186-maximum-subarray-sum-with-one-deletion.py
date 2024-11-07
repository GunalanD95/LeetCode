from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        N = len(nums)
        
        if N == 1: 
            return nums[0]
        
        max_sum = float('-inf')
        
        cur_sum = nums[0]
        max_sum_no_deletion = nums[0] 
        max_sum_with_deletion = float('-inf')  
        
        for right in range(1, N):
            max_sum_no_deletion = max(nums[right], max_sum_no_deletion + nums[right])
            max_sum_with_deletion = max(max_sum_with_deletion + nums[right], cur_sum)
            cur_sum = max_sum_no_deletion
            max_sum = max(max_sum, max_sum_no_deletion, max_sum_with_deletion)
        
        return max_sum