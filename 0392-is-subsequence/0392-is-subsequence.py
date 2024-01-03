from collections import *

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        j = 0
        N , M = len(s) , len(t)
        
        while i < N and j < M:
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i ==N else False
        