class Solution:
    def hammingWeight(self, n: int) -> int:
        n = int(n)        
        c = 0
        for i in range(32):
            
            if (1 << i) & n:
                c += 1
                
        return c
            
        