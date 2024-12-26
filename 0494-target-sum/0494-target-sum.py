class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N   = len(nums)
        @cache
        def generate_expr(indx,cur_sum):
            if indx >= N:
                if cur_sum == target:
                    return 1
                return 0
            
            # add plus
            p = generate_expr(indx+1,cur_sum+nums[indx])
            
            # add minus
            n = generate_expr(indx+1,cur_sum-nums[indx])
            
            return p + n
        
        return generate_expr(0,0)
        