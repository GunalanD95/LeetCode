class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        a = 0
        b = 1
        c = 1
        
        val = 0
        for num in range(3,n+1):
            val = a + b + c
            a   = b
            b   = c
            c   = val
        return val