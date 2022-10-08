class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        if N == 1: return heights[0]

        left = [-1] * N
        lstack = []

        for i in range(N):
            while lstack and heights[i] <= heights[lstack[-1]]:
                lstack.pop()
            if lstack:
                left[i] = lstack[-1]
            lstack.append(i)

        right = [N] * N
        rstack = []
        for i in range(N-1,-1,-1):
            while rstack and heights[i] <= heights[rstack[-1]]:
                rstack.pop()
            if rstack:
                right[i] = rstack[-1]
            rstack.append(i)

        ans = float('-inf')
        
        
        for i in range(N):
            val = heights[i] * (right[i] - left[i] - 1)
            
            ans = max(ans,val)
        
        return ans
        
        