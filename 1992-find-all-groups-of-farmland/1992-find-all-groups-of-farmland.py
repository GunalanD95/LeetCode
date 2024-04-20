class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows , cols = len(land) , len(land[0])
        visited = set()
        
        total_islands = []
        
        
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 0 or (row,col) in visited:
                    continue

                start_row , start_col = row,col
                end_row , end_col     = row,col
                

                while end_col < cols and land[row][end_col] == 1:
                    visited.add((row,end_col))
                    end_col += 1
                    
                while end_row < rows and land[end_row][col] == 1:
                    for column in range(start_col,end_col):
                        visited.add((end_row,column))
                    end_row += 1
                
                farm_land = [start_row , start_col,end_row-1,end_col-1]
                
                total_islands.append(farm_land)
            
        return total_islands 