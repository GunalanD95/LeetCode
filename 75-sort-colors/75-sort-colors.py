class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        m = 0
        h = len(nums) - 1

        while m <= h:
            if nums[m] == 1:
                m += 1
                
                
            elif nums[m] == 0:
                temp = nums[m]
                nums[m] = nums[l]
                nums[l] = temp
                m += 1
                l += 1
                
                
                
            elif nums[m] == 2:
                temp = nums[m]
                nums[m] = nums[h]
                nums[h] = temp
                h -= 1
                
                
        return nums
            
                
        