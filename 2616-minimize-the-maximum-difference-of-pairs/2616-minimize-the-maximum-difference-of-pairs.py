class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:  
        if p == 0 or not nums:
            return 0
        
        nums.sort()
        low , high = 0 , nums[-1]
        
        ans = nums[-1]
        
        while low <= high:
            
            mid  = (low + high)//2
            
            pairs = 0
            i = 1
            while i < len(nums):
                if abs(nums[i-1] - nums[i]) <= mid:
                    i += 2
                    pairs += 1
                else:
                    i += 1
                    
            if pairs >= p:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
            
        return ans 