class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.pf = [[0]*cols for i in range(rows)]

        # row wise pf
        for i in range(rows):
            prev = matrix[i][0]
            self.pf[i][0] = matrix[i][0]
            for j in range(1,cols):
                self.pf[i][j] = prev + matrix[i][j]
                prev = self.pf[i][j]

        # col wise pf
        for j in range(cols):
            prev = self.pf[0][j]
            for i in range(1,rows):
                self.pf[i][j] = prev + self.pf[i][j]
                prev = self.pf[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a1 , b1 = row1 , col1 

        a2 , b2 = row2 , col2 

        total_sum = self.pf[a2][b2]          # BOTTOM-RIGHT SUM  (TOTAL PF)


        # removing top part 
        if a1 > 0:
            total_sum -= self.pf[a1-1][b2]

        # removing left part
        if b1 > 0:
            total_sum -= self.pf[a2][b1-1]

        # neutralizing the extra removed part 
        if a1 > 0 and b1 > 0:
            total_sum += self.pf[a1-1][b1-1]    
                 
        return total_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)