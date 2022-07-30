class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == target:
#                     return True
                
#         return False
    
        A = matrix
    
        rows = len(A)
        cols = len(A[0])


        i = 0
        j = cols - 1

        while i < rows and j >= 0:
            if A[i][j] == target:
                return True 
                
            if A[i][j] > target:
                j -= 1
                
            # elif A[i][j] < B:
            else:
                i += 1

        return False
        