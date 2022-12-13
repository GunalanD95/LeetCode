class Solution:
    def minFallingPathSum(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        cols = len(triangle[rows - 1])
        def recurBro(i,j,hmap):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return float('inf')
            
            if i == (rows -1):
                return triangle[i][j]
            
            if (i,j) in hmap:
                return hmap[(i,j)]

            hmap[(i,j)] = triangle[i][j] + min(recurBro(i+1,j,hmap),
                                               recurBro(i+1,j-1,hmap),
                                               recurBro(i+1,j+1,hmap))
            return hmap[(i,j)]
        min_sum = float('inf')
        for i in range(cols):
            min_sum = min(min_sum , recurBro(0,i,{}))
        return min_sum
        
        
        
        
        
        
        
            
            
        