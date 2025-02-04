class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        N = len(nums)
        right   = 1
        cur_sum = nums[0]
        max_sum = cur_sum
        while right < N:
            if nums[right] > nums[right-1]:
                cur_sum += nums[right]
            else:
                cur_sum = nums[right]
            max_sum = max(max_sum,cur_sum)
            right += 1
        return max_sum
