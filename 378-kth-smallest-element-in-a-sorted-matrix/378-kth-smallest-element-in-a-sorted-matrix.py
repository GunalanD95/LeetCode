class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        res = []
        
        for i in range(rows):
            for j in range(cols):
                res.append(matrix[i][j])
                
                
        res.sort()
        return(res[k-1])
        