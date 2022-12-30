class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        numzeroes = 0
        
        
        left = 0
        
        max_len = 0
        
        for right in range(N):
            if nums[right] == 0:
                numzeroes += 1
                
            while numzeroes > k:
                # Shrink the window
                if nums[left] == 0:
                    numzeroes -= 1
                    
                left += 1
                
                
            max_len = max(max_len,right-left+1)
            
            
        return max_len
        