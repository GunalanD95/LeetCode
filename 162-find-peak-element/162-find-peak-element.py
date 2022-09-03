class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        N = len(nums)
        nums.append(float("-inf"))
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]: return i
            
        return 0