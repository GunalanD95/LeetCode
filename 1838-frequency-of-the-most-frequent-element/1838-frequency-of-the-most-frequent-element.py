class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        left = 0
        max_frq  = 1
        prev_sum = 0
        for right in range(N):
            prev_sum += nums[right]
            target   = nums[right]            
            while (right - left + 1) * target - prev_sum > k:
                prev_sum -= nums[left]
                left += 1
            max_frq = max(max_frq,right - left + 1)
        return max_frq
            
            
            
            
            
        