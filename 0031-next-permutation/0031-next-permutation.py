class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        indx = -1
        
        N = len(nums)
        
        for i in range(N-2,-1,-1):
            if nums[i] < nums[i+1]:
                indx = i
                break
        
        
        if indx == -1:
            nums.reverse()
            return  nums
        
        
        for j in range(N-1,indx,-1):
            if nums[indx] < nums[j]:
                nums[indx] , nums[j] = nums[j] , nums[indx]
                break
                
        # Step 3: reverse the right half:
        nums[indx+1:] = reversed(nums[indx+1:])  
        return nums
        