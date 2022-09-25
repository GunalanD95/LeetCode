class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        
        count = 0
        ans = 1
        
        for i in range(len(nums)):
            if nums[i] == max_val:
                count += 1
            else:
                count = 0
                
            ans = max(ans,count)
            
            
        return ans 