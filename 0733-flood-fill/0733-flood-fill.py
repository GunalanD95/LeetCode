from collections import deque

class Solution: 
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        N , M = len(image) , len(image[0])
        
        num   = image[sr][sc]
        
        if num == color:
            return image
        
        def dfs(i , j ):
            print(i,j)
            if i < 0 or j < 0 or i >= N or j >= M:
                return
            
            if image[i][j] != num:
                return
            
            if image[i][j] == num:
                image[i][j] = color
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
                
        
        dfs(sr,sc)
        return image
        