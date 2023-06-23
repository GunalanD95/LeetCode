from typing import List
from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        max_length = 0
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp[(j, diff)] + 1
                max_length = max(max_length, dp[(i, diff)])
        
        return max_length + 1
