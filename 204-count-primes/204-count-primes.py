import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2: 
            return 0
        
        sqr = int(math.sqrt(n))

        pf = [True] * (n+1)

        pf[0] , pf[1] = False ,False

        i =  2
        while i * i < n:
            if pf[i] == True:
                j = i * i 
                while j < n:
                    pf[j] = False
                    j = j + i
                    
            i = i + 1

        c = 0
        for k in range(1,len(pf)):
            if pf[k]:
                c += 1
                
                
        return c - 1
        
        