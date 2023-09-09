class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1 for _ in range(target+1)]
        def solve(tar):
            if tar<0:
                return 0
            if tar == 0:
                return 1
            if dp[tar] != -1:
                return dp[tar]
            ans = 0
            for i in nums:
                ans += solve(tar - i)
            dp[tar] = ans
            return dp[tar]
        return solve(target)