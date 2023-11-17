class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        max_pair = float('-inf')
        for i in range(N//2):
            min_val = nums[i]
            max_val = nums[N-i-1]
            max_pair = max(max_pair,min_val+max_val)
        return max_pair