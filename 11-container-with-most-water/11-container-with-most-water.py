class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # BruteForce
        
#         i = 0
#         N = len(height)
        
#         ans =  -1
#         for i in range(N):
#             j = i + 1
            
#             while j < N:
#                 # min height is the max point within we can store water bw two walls
#                 # area covered is nothing but length of subarray 
                
#                 water_stored = (j-i) * min(height[i],height[j])
                
#                 ans = max(ans,water_stored)
                
#                 j += 1
                
                
#         return ans
    
        # Optimized using Two Pointer 
        
        N = len(height)
        
        i =  0
        j =  N -1
        
        ans = float('-inf')
        
        while i < j:
            
            water_stored = ( j - i ) * min(height[i],height[j])
            
            ans = max(ans,water_stored)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -=1
                
                
        return ans
        