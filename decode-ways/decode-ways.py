class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        
        
        cache = {}
        
        def decode_string(indx):
            if indx >= N:
                return 1
            
            if indx in cache:
                return cache[indx]
            
            total = 0
            for idx in range(indx,N):
                if s[indx] != '0' and int(s[indx:idx+1]) >= 1 and int(s[indx:idx+1]) <= 26:
                    total += decode_string(idx+1)
            
            cache[indx] = total
            return cache[indx]

        return decode_string(0)
        