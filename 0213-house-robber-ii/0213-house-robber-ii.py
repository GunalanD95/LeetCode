class Solution:
    def rob2(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [-1] * (N)
        
        def recurBro(indx):
            if indx < 0:
                return 0
            
            if dp[indx] != -1:
                return dp[indx]
            
            dont_take = recurBro(indx-1)
            
            take_it   = nums[indx] + recurBro(indx-2)
            
            dp[indx] =  max(take_it,dont_take)
        
            return dp[indx]
        
        
        recurBro(N-1)
        return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob2(nums[0:len(nums)-1]),self.rob2(nums[1:]))