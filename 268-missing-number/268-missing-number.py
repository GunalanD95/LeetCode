class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        sumN = N *(N+1)
        sumN = sumN // 2
        
        csum = 0
        for i in nums:
            csum += i
            
        return sumN - csum
        