from functools import cache , lru_cache

class Solution:
    @lru_cache(None)
    def factarr(self,i):
        return 1 if i <= 1 else (self.factarr(i-1)*i) % (10**9+7)

    @lru_cache(None)
    def inv(self, i):
        mod = 10**9 + 7
        return pow(i, mod-2, mod)

    def makeStringSorted(self, s: str) -> int:
        N = len(s)
        
        if N == 1: return 0
        
        mod = 10**9 + 7
        
        out = 0
        counter = [0] * 26
        for i in range(N-1, -1, -1):
            indx = ord(s[i]) - ord("a")
            counter[indx] += 1
            ans = sum(counter[:indx]) * self.factarr(N-i-1)
            
            for j in range(26):
                ans = ans * self.inv(self.factarr(counter[j])) % mod
    
            out += ans  % mod
            
        return out % mod
    
    
    
        '''
        approahc :
        
        https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/discuss/1163050/Python-O(26n)-math-solution-explained
        
        '''
            
            
        
        
        