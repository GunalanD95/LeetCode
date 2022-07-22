class Solution:
    def fib(self, n: int) -> int:
        
        def fib2(n):
            if n == 0 :
                return 0
            if n == 1:
                return 1
            
            return fib2(n-1) + fib2( n- 2)
        
        
        return fib2(n)
        