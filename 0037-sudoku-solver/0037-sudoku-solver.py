from collections import defaultdict
class Solution:
    def insertinMaps(self,value,row,col,rowMap,colMap,sqrMap):
        rowMap[row].add(value)
        colMap[col].add(value)
        sqrMap[(row//3,col//3)].add(value)

    def removeinMaps(self,value,row,col,rowMap,colMap,sqrMap,indx):
        rowMap[row].remove(value)
        colMap[col].remove(value)
        sqrMap[(row//3,col//3)].remove(value)

    def verifyMaps(self,value,row,col,rowMap,colMap,sqrMap):
        if value in colMap[col] or value in rowMap[row] or value in sqrMap[(row//3,col//3)]:
            return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows , cols = 9 , 9
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        sqrMap = defaultdict(set)   # (row//3 , col// 3) 
        
        ans_mat = []
        
        # inserting initial cells in map
        for ii in range(9):
            for jj in range(9):
                if  board[ii][jj] != '.':
                    self.insertinMaps(int(board[ii][jj]),ii,jj,rowMap,colMap,sqrMap) 
                    
        def Sudoku(indx,mat):
            if indx == 81:
                temp_mat = mat.copy()
                ans_mat  = temp_mat
                return True
            
            row = indx // 9           # row indx in matrix
            col = indx % 9            # col indx in matrix
            
            # already filled 
            if mat[row][col] != '.':
                return Sudoku(indx+1,mat)
            else:
                # not filled try all possible numbers
                for cell in range(1,10):
                    if self.verifyMaps(cell,row,col,rowMap,colMap,sqrMap):        # verify cell can be placed
                        self.insertinMaps(cell,row,col,rowMap,colMap,sqrMap)      # if so then add newval in maps
                        mat[row][col] = str(cell)
                        if Sudoku(indx+1,mat):                                    # since we filled call next cell
                            return True
                        
                        # if last call not working undo and backtrack
                        mat[row][col] = '.'
                        self.removeinMaps(cell,row,col,rowMap,colMap,sqrMap,indx)
                        
                return False
            
        Sudoku(0,board)
        return ans_mat
                        
                
                
            
            
            
            
            