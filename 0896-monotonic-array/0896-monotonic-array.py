class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        
        prev = nums[0]
        
        increasing = True
        decreasing = True
        
        for i in range(1,n):
            cur = nums[i]
            
            if cur < prev:
                increasing = False
                break
            
            prev = cur
         
        prev = nums[-1]
        for i in range(n-2,-1,-1):
            cur = nums[i]
            
            if cur < prev:
                decreasing = False
                break
            
            prev = cur
            
            
        return increasing or decreasing
            
        
        