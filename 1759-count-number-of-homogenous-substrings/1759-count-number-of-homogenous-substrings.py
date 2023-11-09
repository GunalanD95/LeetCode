from collections import *

class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = int(1e9) + 7 
        N = len(s)
        left = 0
        res  = 0
        for right , char in enumerate(s):
            if s[left] == char:
                res += right - left + 1
            else:
                left =  right
                res += 1
                
        return res % MOD