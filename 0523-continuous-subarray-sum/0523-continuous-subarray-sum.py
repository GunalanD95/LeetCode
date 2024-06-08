class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur_sum = 0
        
        pf = {0 : -1}
        
        for idx,num in enumerate(nums):
            cur_sum += num
            cur_sum %= k
            
            if cur_sum in pf and (idx - pf[cur_sum]) > 1:
                return True
            
            if cur_sum not in pf:
                pf[cur_sum] = idx
            
            
        return False