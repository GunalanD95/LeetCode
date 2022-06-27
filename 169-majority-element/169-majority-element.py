class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = nums[0]
        c = 0
        
        for i in nums:
            if c == 0:
                me = i
                
            if i == me:
                c += 1
                
            elif i != me:
                c -= 1
                

        
        cc = 0
        for j in nums:
            if j == me:
                cc += 1   
        if cc > len(nums)/2:
            return me
        