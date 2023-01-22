class Solution:
    def hashCode(self,w):
        n = len(w)
        code = 0
        for i in range(n):
            value = ((ord(w[i]) - ord('a') + 1) * self.POW[n-i-1]) 
            code += value
            code %= self.MOD

        return code
            
    
    def strStr(self, haystack: str, needle: str) -> int:
        N,M  = len(haystack) , len(needle)
        
        self.MOD  = 1000000007
        self.base = 27
        
        self.POW  = [1] * (max(N,M)+1)
        
        for i in range(max(N,M)):
            self.POW[i+1] = (self.POW[i] * self.base) % self.MOD
        # given pattern sum
        pattern_hash = self.hashCode(needle)
        #hash_sum for first M window 
        hash_yellow  = self.hashCode(haystack[:M])
        
        if pattern_hash == hash_yellow: return 0
        
        low = 0 
        right = M
        while right < N:
            
            hash_yellow -= (ord(haystack[low]) - ord('a') + 1) * self.POW[M-1]
            
            hash_yellow *= (self.base)  % self.MOD
            
            hash_yellow %=  self.MOD
            
            
            hash_yellow += (( ord(haystack[right]) - ord('a') + 1 ))
            
            
            if hash_yellow == pattern_hash:
                return low + 1
            
            low   += 1
            right += 1
            
            
        return -1
            
        
        
            
        
        