class Solution:
    def hammingWeight(self, n: int) -> int:
        n = int(n)
        # def checkbit(i,n):
        #     mask = 1 << i
        #     return mask & n
        
        c = 0
        for i in range(32):
            # res = checkbit(i,n)
            
            if (1 << i) & n > 0:
                c += 1
                
        return c
            
        