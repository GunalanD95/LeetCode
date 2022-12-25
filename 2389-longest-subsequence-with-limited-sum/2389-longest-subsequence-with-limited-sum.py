class Solution:
    def searchInsert(self,nums,target):
        low   = 0 
        high  = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid -1 
            else:
                low  = mid + 1
                
        return high
        
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n  = len(nums)
        
        nums.sort()
        pf = [0] * (n)
        pf[0] = nums[0]
        
        for i in range(1,n):
            pf[i] = pf[i-1] + nums[i]
            
        ans = []
        
        for q in queries:
            indx = self.searchInsert(pf,q)
            ans.append(indx+1)
            
        return ans         