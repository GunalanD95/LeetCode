class Solution:        
    def search(self, nums: List[int], target: int) -> bool:
        
        low , high = 0 ,len(nums) - 1
        
        
        while low <= high:
            mid = (low + high)//2
            
            print("mid",mid,"nums[mid]",nums[mid])
            if nums[mid] == target:
                return True 
            
            
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
            
            # left side is sorted
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid] :
                    high = mid - 1
                else:
                    low  = mid + 1
            
            else:
                if nums[mid] <= target  <= nums[high]:
                    low  = mid + 1
                else:
                    high = mid - 1                
                
            
            
            
        return False
        