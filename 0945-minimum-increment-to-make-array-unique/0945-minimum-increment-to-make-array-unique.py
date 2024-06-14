class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        count = 0
        for i in range(1,N):
            if nums[i] <= nums[i-1]:
                temp = nums[i]
                nums[i] = nums[i-1] + 1
                count += nums[i] - temp
                
                
        return count
        
        
        '''
        
        Algorithm:
    1. As all elements sorted, I just increase current element by 1, if it equals or less than the previous element in array and i continue this process untill current element becomes greater than previous element as all elements should be unique.
        
        '''
        