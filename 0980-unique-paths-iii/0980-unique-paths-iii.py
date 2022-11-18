class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.count  = 0
        i = len(grid)     # row
        j = len(grid[0])  # col
        ans = []
        empty = 1
        start = [0,0]
        for ii in range(i):
            for jj in range(j):
                if grid[ii][jj] == 1:
                    start[0] = ii
                    start[1] = jj 

                if grid[ii][jj] == 0:
                    empty += 1 
                    
        print("start_point",start,"empty",empty)
        
        def ratinMaze(row,col,mat,empty):
            if row < 0 or row >= i or  col < 0 or col >= j:
                return False
            
            # blocked
            if mat[row][col] == -1:
                return False
            
            if mat[row][col] == 2:
                print("yes",row,col,empty)
                if empty == 0:
                    self.count += 1
                return 

            # mark it as visited
            mat[row][col] = -1
            
            # go top 
            ratinMaze(row-1,col,mat,empty-1)      
            # go down 
            ratinMaze(row+1,col,mat,empty-1)  
            # go left 
            ratinMaze(row,col-1,mat,empty-1)  
            # go right 
            ratinMaze(row,col+1,mat,empty-1)  
            

            # undo changes
            mat[row][col] = 0
            
            
            
        ratinMaze(start[0],start[1],grid,empty)  
        
        return self.count
        