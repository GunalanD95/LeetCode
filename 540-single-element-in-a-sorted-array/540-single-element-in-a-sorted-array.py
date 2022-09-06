class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        # edge cases
        
        if nums[0] != nums[1]: return nums[0]
        if nums[N-1] != nums[N-2]: return nums[N-1]
        
        low = 1
        high = N -2
        
        while low <= high:
            
            mid = (low + high)// 2
            
            
            # finding first occurence index value 
            
            firstocc = mid 
            
            if nums[mid] == nums[mid -1]:
                firstocc = mid - 1
            
            
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            
            if firstocc % 2 == 0:
                low = mid + 1
                
            else:
                high = mid - 1
        
        