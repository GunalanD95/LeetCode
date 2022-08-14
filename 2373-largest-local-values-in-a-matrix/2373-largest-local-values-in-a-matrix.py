class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        N = len(grid)

        res = [[0]*(N-2) for i in range(N-2)]

        for x in range(N-2):
            for y in range(N-2):
                max_val = 0
                for xx in range(x,x+3):
                    for yy in range(y,y+3):
                        ans = grid[xx][yy]
                        max_val = max(ans,max_val)
                        
                res[x][y] = max_val

        return res
