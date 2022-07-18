class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        N = len(mat)
        res = 0
        row = len(mat)
        col = len(mat[0])
        
        s = 0
        e = 0
        
        while s <= N-1 and e <= N-1:
            res += mat[s][e]
            s+=1
            e+=1
                    
        r = 0
        c = N - 1 
        
        while r <= N - 1 and c >=0:
            if r != c:
                res += mat[r][c]
            r += 1
            c -= 1
            
        return res
        
        