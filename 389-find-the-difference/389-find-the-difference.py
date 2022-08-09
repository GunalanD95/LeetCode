class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        ans = 0
        
        for i in range(len(s)):
            ans ^= ord(s[i])
            
            
        for j in range(len(t)):
            ans ^= ord(t[j])
            
            
        return(chr(ans))