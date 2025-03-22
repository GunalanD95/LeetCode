from collections import Counter

class Solution:
    def check_palindrome(self,string,l,r):
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True


    def validPalindrome(self, s: str) -> bool:
        N  = len(s)
        
        l , h  = 0 , N-1
        while l < h:
            if s[l] != s[h]:
                check_left  = self.check_palindrome(s,l,h-1)
                check_right = self.check_palindrome(s,l+1,h)
                if not check_left and not check_right:
                    return False
                else:
                    return True
            l += 1
            h -= 1
        return True
        
