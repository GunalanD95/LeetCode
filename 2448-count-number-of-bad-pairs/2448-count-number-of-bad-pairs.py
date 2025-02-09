from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        count = defaultdict(int)
        good_pairs = 0

        # Count occurrences of (nums[i] - i)
        for i in range(N):
            key = nums[i] - i
            good_pairs += count[key]  # Add existing count to good pairs
            count[key] += 1  # Update frequency

        total_pairs = N * (N - 1) // 2
        return total_pairs - good_pairs
