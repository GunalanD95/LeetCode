class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @cache
        def check(s1,s2):
            if s1 == s2:
                return True
            
            L = len(s1)
            
            for i in range(1,L):
                if check(s1[0:i],s2[0:i]) and check(s1[i:],s2[i:]):
                    return True
                
                if check(s1[0:i],s2[L-i:]) and check(s1[i:],s2[0:L-i]):
                    return True
                
            return False
        
        return check(s1,s2)
            
        