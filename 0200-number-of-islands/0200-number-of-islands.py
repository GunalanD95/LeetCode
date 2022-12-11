class Solution:
    def backtracking(self,i,j,mat,N,M):
        if i < 0 or i >= N or j < 0 or j >= M:
            return 
        
        if mat[i][j] == '0':
            return 
        
        if mat[i][j] == '1':
            mat[i][j] = '0'               # make it visited 
            
            # go top 
            self.backtracking(i-1,j,mat,N,M)
            # go down
            self.backtracking(i+1,j,mat,N,M)
            # go right
            self.backtracking(i,j+1,mat,N,M)
            # go left
            self.backtracking(i,j-1,mat,N,M)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        N , M = len(grid) , len(grid[0])
        
        islands = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    self.backtracking(i,j,grid,N,M)
                    islands += 1
                     
                    
        return islands
                    
        