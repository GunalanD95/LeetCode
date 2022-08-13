class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minval = min(nums)
        maxval = max(nums)
        
        def gcd(A,B):
            rng = min(A,B)

            i = rng 

            while i > 0:
                if A % i == 0 and B % i == 0:
                    return i 

                i -= 1

            return 1
        
        val = gcd(minval,maxval)
        return val
        