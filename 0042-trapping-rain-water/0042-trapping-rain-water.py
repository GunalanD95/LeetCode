class Solution:
    def trap(self, height: List[int]) -> int:
        
        N = len(height)
        
        #lmax array
        lmax = []
        lmaxval = float('-inf')
        for i in range(N):
            if height[i] > lmaxval:
                lmaxval = height[i]
            lmax.append(lmaxval)
        
        #rmax array
        rmax = []
        s = N -1
        rmaxval = height[-1]
        while s >=0:
            if height[s] > rmaxval:
                rmaxval = height[s]
            rmax.append(rmaxval)
            s -=1
            
        rmax = rmax[::-1]
        waterstored = 0
        for i in range(N):
            val = min(lmax[i],rmax[i])
            waterstored += val - height[i]
        return waterstored