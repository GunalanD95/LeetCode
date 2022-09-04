class Solution:
    
    def findminindx(self,arr,k):
        low = 0
        high = len(arr) - 1

        mindx = - 1

        while low <= high:

            mid = (low + high) // 2


            if arr[mid] >= k:
                if arr[mid] == k:
                    mindx = mid 

                high = mid - 1

            if arr[mid] < k:
                low = mid + 1

        return mindx
    
    def findmaxidx(self,arr,k):
        low = 0
        high = len(arr) - 1

        maxidx = - 1

        while low <= high:

            mid = (low + high) // 2


            if arr[mid] <= k:
                if arr[mid] == k:
                    maxidx = mid 
                low = mid + 1

            if arr[mid] > k:
                high = mid - 1

        return maxidx
    
    

    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min_index = self.findminindx(nums,target)
        max_index = self.findmaxidx(nums,target)
        
        return [min_index,max_index]
        
        