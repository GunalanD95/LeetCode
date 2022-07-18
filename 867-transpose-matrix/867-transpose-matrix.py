class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row = len(matrix)
        
        col = len(matrix[0])
        
        arr = [[0]*row for i in range(col) ]
        
        for i in range(row):
            for j in range(col):
                arr[j][i] = matrix[i][j]
        return arr