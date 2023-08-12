class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        i = len(obstacleGrid) # row
        j = len(obstacleGrid[0])
        
        hashmap = defaultdict(set)
        
        def ratinMaze(row,col,mat,hashmap):
            if row > i-1 or col > j-1:        # out of bounds
                return 0 
            
            
            if mat[row][col] == 1:            # blocked
                return 0
            
            if row == i-1 and col == j-1:     # ans
                return 1
            
            if (row,col) not in hashmap:
                hashmap[(row,col)] = ratinMaze(row,col+1,mat,hashmap) + ratinMaze(row+1,col,mat,hashmap)
            
            return hashmap[(row,col)]

        return ratinMaze(0,0,obstacleGrid,hashmap)  