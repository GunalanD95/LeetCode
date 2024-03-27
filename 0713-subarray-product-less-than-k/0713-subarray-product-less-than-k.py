class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        N = len(nums)
        
        count = 0
        low   = 0
        cur_prod = 1
        
        for high in range(N):
            cur_prod *= nums[high]
            
            # cut down from left
            while cur_prod >= k:
                cur_prod //= nums[low]
                low += 1
                
            count += high - low + 1
            
        return count
