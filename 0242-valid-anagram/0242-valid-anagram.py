from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        smap = defaultdict(int)
        tmap = defaultdict(int)
        
        for char in s:
            smap[char] += 1
            
        for char in t:
            tmap[char] += 1
            
        
        if len(smap) != len(tmap):
            return False
        
        
        for char in smap:
            if char not in tmap or smap[char] != tmap[char]:
                return False
        return True
        