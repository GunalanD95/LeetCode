class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sn = len(s) 
        tn = len(t) 

        i = 0
        j = 0

        while i < sn and j < tn:
            if s[i] == t[j]:
                i +=1
            j+= 1

        if i != sn:
            return False
        else:
            return True