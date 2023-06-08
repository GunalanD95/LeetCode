class Solution:
    
    def binarysearch(self,arr):
        low , high = 0 , len(arr) - 1
        
        ans = -1
        while low <= high:
            mid  = (low + high) // 2
            if arr[mid] >= 0:
                low = mid + 1
            else:
                ans  = mid
                high = mid - 1

        return ans
        
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        N , M = len(grid) , len(grid[0])
        
        
        for row in grid:
            value = self.binarysearch(row)
            if value != -1:
                neg   += (M - value)
        
        return neg
        