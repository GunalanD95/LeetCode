class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pf , res = 0 , 0
        for num in nums:
            pf += num
            res = min(res,pf)
        return abs(res) + 1
        