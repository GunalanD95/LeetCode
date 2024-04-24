class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        
        col = len(matrix[0])
        
        def rev(A):
            N = len(A)
            s = 0
            e = N - 1
            while s <= e:
                temp = A[s]
                A[s] = A[e]
                A[e] = temp
                s += 1
                e -=1
            return A
        
        
        
        # TRANSPOSE THE MATRIX
        
        for i in range(row):
            for j in range(i+1,col):
                temp = matrix[i][j] 
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
                
        # REVERSE EACH ROW
        
        for k in range(row):
            rev(matrix[k])
                
        