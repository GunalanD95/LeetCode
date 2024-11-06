from collections import defaultdict

class Solution:
    def countSetBits(self, num):
        return bin(num).count('1')
    
    def canSortArray(self, nums):
        N = len(nums)
        
        
        set_bits = [self.countSetBits(num) for num in nums]
        
        
        cur_min_val = nums[0]
        cur_max_val = nums[0]
        
        pre_max = float('-inf')
        
        for i in range(1,N):
            if set_bits[i-1] == set_bits[i]:
                cur_max_val = max(nums[i],cur_max_val)
                cur_min_val = min(nums[i],cur_min_val)
            else:
                if cur_min_val < pre_max:
                    return False
                
                
                pre_max = cur_max_val
                cur_min_val = nums[i]
                cur_max_val = nums[i]
                
        if cur_min_val < pre_max:
            return False
                
        return True
            
            
                
        
