class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pf_sum = 0

        hmap = {0: 1}
        total = 0
        for idx,num in enumerate(nums):
            pf_sum += num
            
            if pf_sum - goal in hmap:
                total += hmap[pf_sum - goal]
            
            if pf_sum in hmap:
                hmap[pf_sum] += 1
            else:
                hmap[pf_sum] = 1
                
            
        return total