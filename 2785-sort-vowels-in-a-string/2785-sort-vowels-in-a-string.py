class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        N = len(s)
        
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        indexs = []
        v_chrs = []

        for idx,char in enumerate(s):
            if char in vowels:
                indexs.append(idx)
                v_chrs.append(ord(char))
        v_chrs.sort()

        for i in range(len(indexs)):
            indx = indexs[i]
            char = chr(v_chrs[i])
            
            s[indx] = char
            
        return "".join(s)