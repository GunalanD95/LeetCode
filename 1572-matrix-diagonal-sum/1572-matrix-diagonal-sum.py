class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        N = len(mat)
        res = 0
        row = len(mat)
        col = len(mat[0])
        
        for i in range(row):
            for j in range(col):
                if i == j:
                    res += mat[i][j]
                    
        r = 0
        c = N - 1 
        
        while r <= N - 1 and c >=0:
            if r != c:
                res += mat[r][c]
            r += 1
            c -= 1
            
        return res
        
        