class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = nums[0]
        for i in range(1,len(nums)):
            res[i] *= pre
            pre *= nums[i]


        pre = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            res[i] *= pre
            pre *= nums[i]     
            
        return res