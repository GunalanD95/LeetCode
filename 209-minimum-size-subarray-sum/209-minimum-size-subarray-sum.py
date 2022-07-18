class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        N = len(nums)

        
        res = float("inf")
        
        l = 0
        r = 0
        cur_sum = 0
        while r <= N -1:
            cur_sum += nums[r]
            while cur_sum >= target:
                length = r - l + 1
                res = min(res,length)
                cur_sum -= nums[l]
                l += 1
            r += 1
            
        if res == float("inf"):
            return 0
        else:
            return res 
        
        
        