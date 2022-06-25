class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(n):
            if n > 0:
                return 1
            elif n == 0:
                return 0
            else:
                return -1
            
        ans = 1
        for i in nums:
            ans *= i
        return signFunc(ans)
        