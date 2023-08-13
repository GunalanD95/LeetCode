from functools import lru_cache

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @lru_cache(None)
        def Partition(indx):
            if indx == n:
                return True
            
            # 3 cases 
            # equal case ( len(2)  and len(3) )
            if indx+1 < n and nums[indx] == nums[indx+1]:
                if Partition(indx+2):
                    return True
                if indx+2 < n and nums[indx] == nums[indx+2] and Partition(indx+3):
                    return True 
                
            # inc case ( len(3) )
            if indx+2 < n and 1+nums[indx] ==  nums[indx+1] and 1+nums[indx+1] == nums[indx+2]:
                if Partition(indx+3):
                    return True
                
            return False
        return Partition(0)
  