class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        
        suffix = '$'+ s[::-1]
        suf_string = s + suffix
        
        lps = [0] * len(suf_string)
        
        i , j = 0 , 1
        
        while j < len(lps):
            if suf_string[i] == suf_string[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i > 0:
                    i = lps[i-1]
                else:
                    j += 1
                    
                    
        reversed_string = s[::-1]
        return reversed_string[:N-lps[-1]] + s
                
                