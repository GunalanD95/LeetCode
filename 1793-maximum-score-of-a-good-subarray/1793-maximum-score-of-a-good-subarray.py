class Solution:
    def maximumScore(self, nums, k):
        def test(nums, k):
            left  = list(accumulate(nums[:k+1][::-1], min))[::-1]
            right = list(accumulate(nums[k:], min))
            ans = 0
            for j in range(0, len(right)):
                i = bisect_left(left, right[j])
                if i >= 0: ans = max(ans, (k + j - i + 1) * right[j] )

            return ans

        return max(test(nums, k), test(nums[::-1], len(nums) - k - 1))