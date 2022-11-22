class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_min_prd = nums[0]
        prev_max_prd = nums[0]
        
        cur_min_prod = nums[0]
        cur_max_prod  = nums[0]
        
        N  = len(nums)
        ans = nums[0]
        
        for i in range(1,N):
            cur_min_prod = min(cur_min_prod * nums[i], prev_max_prd * nums[i], nums[i])
            cur_max_prod = max(cur_max_prod * nums[i], prev_min_prd * nums[i] , nums[i])
            
            ans = max(cur_max_prod,ans)
            
            prev_min_prd = cur_min_prod
            prev_max_prd = cur_max_prod
            
            
        print("ans",ans)
            
        return ans 
        
            
            