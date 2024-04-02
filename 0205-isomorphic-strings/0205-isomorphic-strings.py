from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smapper = defaultdict(str)
        tmaper  = defaultdict(str)
        
        for indx in range(len(s)):
            schar = s[indx]
            tchar = t[indx]
            
            if schar not in smapper:
                smapper[schar] = tchar
            else:
                if smapper[schar] != tchar:
                    return False
                
            if tchar not in tmaper:
                tmaper[tchar] = schar
            else:
                if tmaper[tchar] != schar:
                    return False
                
                
        return True