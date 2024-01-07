class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        total_vals = 0

        dp = [defaultdict(int) for _ in range(N)]

        for i in range(N):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1  # Count subsequences ending at index i with difference diff
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]  # Extend the subsequences

                # If there are at least 3 elements forming an arithmetic subsequence,
                # increment the total count.
                if dp[j][diff] > 0:
                    total_vals += dp[j][diff]

        return total_vals        