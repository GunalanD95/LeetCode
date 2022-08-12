class Solution:
    def myPow(self, x: float, n: int) -> float:
#         def calpower(x,n):
#             if n == 0:
#                 return 1
            
#             if n < 0:
#                 return 1 / calpower(x, -n)
            
#             hp = calpower(x,n//2)
            
#             if n % 2 == 0:
#                 return hp * hp
#             else:
#                 return hp * hp * x

        # iterative approach 
        def calpower(a,n):
            res =  1
            
            while n > 0:
                if n % 2 == 1:
                    res = res * a
                a = a * a
                n = n // 2
                
            return res
            
        
        
        if n <  0:
            val = 1 /calpower(x,- n)
        else:
            val = calpower(x,n)
        
        return val