class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = nums[0]
        c = 0
        
        for i in nums:
            if i == me:
                c += 1
            else:
                if c == 0:
                    me = i
                else:
                    c -= 1
        return me
        