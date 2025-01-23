from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        rowmap = defaultdict(int)
        colmap = defaultdict(int)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    rowmap[row] += 1
                    colmap[col] += 1
        total = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and ((rowmap[row] > 1) or colmap[col] > 1):
                    total += 1

        return total        