from collections import Counter, defaultdict
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        hmap = Counter(nums)

        # Step 1: Find the globally dominant element
        dominant = None
        for num, freq in hmap.items():
            if freq > N // 2:
                dominant = num
                break

        if not dominant:
            return -1  # No valid split possible

        left_count = 0
        for idx, num in enumerate(nums):
            if num == dominant:
                left_count += 1

            right_count = hmap[dominant] - left_count

            if left_count > (idx + 1) // 2 and right_count > (N - idx - 1) // 2:
                return idx

        return -1
