from collections import defaultdict
class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, N):
        mat = []
        for i in range(N):
            val = ["."] * N
            mat.append(val)
        ans  = []
        colset = set()
        diag1  = set()   # r-c
        diag2  = set()   # r+c

        def getQueen(row,mat):                
            if row == N:
                copy = ["".join(each_row) for each_row in mat]
                ans.append(copy)
                return 
            
            for col in range(N):
                if col in colset or (row-col) in diag1 or (row+col) in diag2:
                    continue
                    
                
                colset.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                mat[row][col] = "Q"
                
                getQueen(row+1,mat)
                
                # UNDO AND BACKTRACK 
                mat[row][col] = "."
                colset.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                
                
        getQueen(0,mat)
        return ans 
        