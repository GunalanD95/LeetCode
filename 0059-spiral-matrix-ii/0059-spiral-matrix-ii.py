class Solution:
    def spiralOrder(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        top , left    = 0 , 0
        right , down  = cols -1 , rows -1 

        res = []
        dir = 'r'
        val = 1
        while top <= down and left <= right:
            if dir == 'r':
                for i in range(left,right+1):
                    matrix[top][i] = val
                    val += 1
                top += 1
                dir = 'd'

            elif dir == 'd':
                for i in range(top,down+1):
                    matrix[i][right] = val
                    val += 1
                right -= 1
                dir = 'l'

            elif dir == 'l':
                start = right
                end   = left 
                while start >= end:
                    matrix[down][start] = val
                    val += 1
                    start -= 1
                down -= 1
                dir  = 't'

            elif dir == 't':
                start =  down
                end   =  top

                while start >= end:
                    matrix[start][left] = val
                    val += 1
                    start -= 1

                left += 1
                dir  = 'r'

    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        self.spiralOrder(mat)
        return mat