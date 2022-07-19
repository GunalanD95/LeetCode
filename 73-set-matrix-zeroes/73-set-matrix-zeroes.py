class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        rows = len(matrix)
        cols = len(matrix[0])

        rowindx = set()
        colindx = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowindx.add(i)
                    colindx.add(j)


        for i in range(rows):
            for j in range(cols):
                if i in rowindx or j in colindx:
                    matrix[i][j] = 0
                    
                    
                    
        
        