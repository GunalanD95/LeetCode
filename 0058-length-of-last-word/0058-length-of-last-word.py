class Solution:
    def find_len(self,indx,char):
        count = 0
        while indx >= 0:
            if char[indx].isalpha():
                count += 1
                indx -= 1
            else:
                break
        return count
    
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0 
        
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                return self.find_len(i,s)
        