from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        
        def comp(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
            
        nums = sorted(nums,key=cmp_to_key(comp))
        if nums[0] == '0':
            return "0"
        return "".join(nums)
        