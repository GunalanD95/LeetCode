class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337 
#         def calpow(a,n):
#             if n == 0:
#                 return 1
#             elif n < 0:
#                 return 1 / calpow(a, -n) %mod
            
#             halfpow = calpow(a,n//2)
            
#             if n % 2 == 0:
#                 return (halfpow %mod * halfpow %mod ) %mod
#             else:
#                 return (halfpow %mod * halfpow %mod * a %mod) %mod
            
            
        def calpow(a,n):
            res =  1
            
            while n > 0:
                if n % 2 == 1:
                    res = (res % mod * a % mod )  % mod
                a = (a % mod * a % mod) % mod
                n = n // 2
                
            return res
            
            
            
        val = ''.join(map(str, b))
        return calpow(a,int(val)) % mod
        