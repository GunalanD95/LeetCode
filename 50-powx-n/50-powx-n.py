class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calpower(x,n):
            if n == 0:
                return 1
            
            if n < 0:
                return 1 / calpower(x, -n)
            
            hp = calpower(x,n//2)
            
            if n % 2 == 0:
                return hp * hp
            else:
                return hp * hp * x
            
        return calpower(x,n)