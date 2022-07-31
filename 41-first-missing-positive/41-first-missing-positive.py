class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        # BruteForce - Linear Search - O(n)2
        N = len(nums)
        
#         for i in range(1,N+1):
#             if i not in nums:
#                 return i
            
#         return N + 1
    
    
        # Using Boolean Array Method
        
        barr = [False] * (N+1)
        
        for i in nums:
            if i >= 0 and i <= N:
                barr[i] = True
                
                
        for j in range(1,len(barr)):
            if barr[j] == False:
                return j
            
            
        return N + 1
        
                
                
        