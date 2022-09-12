class Solution:
    
    def binarysearch(self,arr,l,r,k):
        low , high = l , r 
        
        while low <= high:
            
            mid = (low + high)//2
            
            if arr[mid] == k:
                return True
            
            if arr[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
            
            
        return False
    
    
    def findPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        nums.sort()
        
        count = 0
        for i in range(N):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
                
            cur_element = nums[i]
            
            # arr[j] - arr[i] == k
            # arr[j] = k + arr[i]
            target = k + nums[i]
            
            start = i + 1
            end = len(nums) - 1
            check_target_exit = self.binarysearch(nums,start,end,target)
            
            if check_target_exit:
                count += 1
                
                
        return count 