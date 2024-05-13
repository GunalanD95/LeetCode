class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        N , M = len(grid) , len(grid[0])
        
        # ok idea to maximse the answer , lets flip all the row at col 0 
        
        
        rowSet = set()
        total_sum = 0
        
        for row in range(N):
            # needs to flip
            if grid[row][0] == 0:
                for col in range(M):
                    grid[row][col] = 1 - grid[row][col]
                
                
        # now lets flip all the cols if it has less zeros , if the col has more zeros then flip it 
        for col in range(1,M):
            cur_ones = 0
            for row in range(N):
                cur_ones += grid[row][col]
            if cur_ones < N/2:
                for row in range(N):
                    grid[row][col] = 1 - grid[row][col]
            
        for row in grid:
            binary_string = ''.join(map(str, row))
            binary_value = int(binary_string, 2)
            total_sum += binary_value
            
        return total_sum
