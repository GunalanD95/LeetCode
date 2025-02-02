class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True  
        
        count = 0  
        n = len(nums)

        for i in range(n - 1):  
            if nums[i] > nums[i + 1]:  
                count += 1 
                if count > 1: 
                    return False
        
        if nums[-1] > nums[0]:
            count += 1
            if count > 1:
                return False

        return True
