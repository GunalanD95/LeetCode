from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        N = len(s)
        
        smap = Counter(s)
        tmap = Counter(t)
        
        
        total = 0
        
        for char in set(s+t):
            total += abs(smap[char] - tmap[char])
            
        return total//2
        