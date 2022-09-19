class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        i = 0
        j = N - 1

        count = 0
        while i < j:
            if s[i] != s[j]:
                check_left = self.checkpalindrome(s,i,j-1)
                check_right = self.checkpalindrome(s,i+1,j)
                if not check_left and not check_right:
                    return False
                else:
                    return True 
            i += 1
            j -= 1 
            
            
        return True 


    def checkpalindrome(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    