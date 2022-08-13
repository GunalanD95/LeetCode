class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        # BruteForce
        minval = min(nums)
        maxval = max(nums)
        
#         def gcd(A,B):
#             i = A 
#             while i * i > 0:
#                 if A % i == 0 and B % i == 0:
#                     return i 

#                 i -= 1

#             return 1
        
        def gcd(A, B):
            if B == 0:
                return A

            return gcd(B,A%B)
        
        val = gcd(minval,maxval)
        return val
        