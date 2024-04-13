class Solution:
    def largestRectangleArea(self,heights):
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
            res = heights[i] * (right[i] - left[i] - 1)
            ans = max(res,ans)
        return ans
                
        
            
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = [0] * cols
        res = float('-inf')
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1': ans[j] += 1
                else: ans[j] = 0
            value = self.largestRectangleArea(ans)
            res = max(res,value)
        return res