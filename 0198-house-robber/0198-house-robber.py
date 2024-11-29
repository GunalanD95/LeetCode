class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        
        max_profit = 0
        
        @cache
        def steel_all(indx,cur_profit):
            nonlocal max_profit
            if indx >= N:
                max_profit = max(max_profit,cur_profit)
                return
            
            # dont steal cur_house
            steel_all(indx+1,cur_profit)
            
            # steel cur_house
            steel_all(indx+2,cur_profit+nums[indx])
        
        
        
        steel_all(0,0)
        return max_profit