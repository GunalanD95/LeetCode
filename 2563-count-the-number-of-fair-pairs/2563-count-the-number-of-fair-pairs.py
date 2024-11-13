from typing import List
import bisect

class Solution:    
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int: 
        # Sort the list to enable efficient range searching
        nums.sort()
        total_pairs = 0
        n = len(nums)
        
        # Iterate over each element in the sorted list
        for i in range(n - 1):
            num = nums[i]
            
            # Find the lower bound index for the pair
            left = bisect.bisect_left(nums, lower - num, i + 1)
            # Find the upper bound index for the pair
            right = bisect.bisect_right(nums, upper - num, i + 1)
            
            # Count pairs within this range
            total_pairs += right - left
        
        return total_pairs
