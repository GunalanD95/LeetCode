class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        N = len(nums)
        
        s , e = 0 , N -1
        
        while s <= e:
            mid = (s+e) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                e = mid - 1
                
            else:
                s = mid + 1
                
                
        return -1
        