class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        # BRUTEFORCE 
        
        A = nums[:]
        A.sort()
        

        minindx = float('inf')
        maxindx = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if A[i] != nums[i]:
                minindx = min(minindx,i)
                maxindx = max(maxindx,i)
        
        if maxindx == float('-inf') or minindx == float('inf'): return 0
        
        return maxindx - minindx + 1