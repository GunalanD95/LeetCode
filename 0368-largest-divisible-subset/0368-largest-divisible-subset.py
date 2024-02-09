from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        N = len(nums)
        dp = [[] for _ in range(N)]  # dp[i] stores the largest subset that ends with nums[i]
        dp[0] = [nums[0]]  # Base case

        for i in range(1, N):
            max_subset = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(max_subset):
                    max_subset = dp[j] + [nums[i]]
            dp[i] = max_subset

        return max(dp, key=len)