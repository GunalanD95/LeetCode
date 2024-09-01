from collections import deque
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        
        matrix = [[None]*n for i in range(m)]
        
        values = deque(original)
        for i in range(m):
            for j in range(n):
                matrix[i][j] = values.popleft() 
                
        return matrix
        
        