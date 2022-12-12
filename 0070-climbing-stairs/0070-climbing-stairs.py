
class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1] * (n+1)
        
        def fibo(n,dp_arr):
            # base case
            if n <= 1:
                return 1
            
            # result not yet calculated
            if dp_arr[n] == -1:
                dp_arr[n] = fibo(n-1,dp) +  fibo(n-2,dp)
                
            return dp_arr[n]
        
        
        return fibo(n,dp)
            
        
        
        "fib(n) = fib(n-1) + fib(n-2)"
        'ans    = prev_ans + prev_p_ans'
        
        