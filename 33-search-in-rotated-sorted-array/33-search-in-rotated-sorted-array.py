class Solution:
    def binarysearch(self,arr,l,r,k):
        low , high = l , r
        
        while low <= high:
            mid = (low + high)//2
            
            if arr[mid] == k: return mid
            
            if arr[mid] > k: high = mid - 1
            else: low =  mid + 1
                
        return -1
            
        
        
    
    def findPOR(self,arr):
        low , high = 0 , len(arr) - 1

        low = 0
        high = len(arr) - 1
        while low <= high:

            mid = low + (high - low)//2

            if arr[mid] < arr[high]:
                high = mid

            else:
                low = mid + 1

        return mid
            
    
    
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums) 
        
        if N == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        POR = self.findPOR(nums)
        
        index1 = self.binarysearch(nums,0,POR-1,target)
        if index1 != -1:
            return index1
        
        index2 = self.binarysearch(nums,POR,N-1,target)
        if index2 != -1:
            return index2            
        return -1
            
        