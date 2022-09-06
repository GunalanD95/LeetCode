class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return 0
        
        if nums[0] > nums[1]:   return 0
        
        elif nums[-1] > nums[-2]: return N - 1
        
        
        low = 1
        high =  N - 2
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid-1] > nums[mid]:
                high = mid - 1
                
            else:
                low  = mid + 1
        
        