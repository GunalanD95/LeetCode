class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N = len(grid)
        rows = len(grid)
        cols = len(grid[0])
        
        arr = [[0]*rows for i in range(cols) ]
        
        # transpose the matrix
        for k in range(cols):
            x = 0
            y = k
            
            while x < N and y <= cols:
                arr[y][x] = grid[x][y]
                x += 1

        # check rows are same 
        c = 0
        for row in grid:
            for col in arr:
                if row == col:
                    c += 1
                
        return c

        
                
                