from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows , cols = 9 , 9
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        sqrMap = defaultdict(set)   # (row//3 , col// 3) 
        
        # check in row an col
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                    
                if board[i][j] in colMap[j] or board[i][j] in rowMap[i] or board[i][j] in sqrMap[(i//3,j//3)]:
                    return False

                rowMap[i].add(board[i][j])
                colMap[j].add(board[i][j])
                sqrMap[(i//3,j//3)].add(board[i][j])   
                
        return True

        
        
        