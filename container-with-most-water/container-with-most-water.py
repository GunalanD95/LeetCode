class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        i = 0
        j = N-1
        max_water_stored = 0
        while i < j:
            min_val  = min(height[i],height[j])
            cur_stored = (j-i) * min_val
            max_water_stored = max(cur_stored,max_water_stored)
            
            if min_val == height[i]:
                i += 1
            else:
                j -= 1
                
        # print("max_water_stored",max_water_stored)
        return max_water_stored