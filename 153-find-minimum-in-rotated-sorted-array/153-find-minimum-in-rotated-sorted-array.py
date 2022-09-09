class Solution:
    
    def POR(self,arr):

        low = 0
        high = len(arr) - 1
        while low <= high:

            mid = low + (high - low)//2

            if arr[mid] < arr[high]:
                high = mid

            else:
                low = mid + 1

        return mid
            
    
    def findMin(self, nums: List[int]) -> int:
        
        POR = self.POR(nums)
        return nums[POR]