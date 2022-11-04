class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        lw = 0
        hg = len(s) - 1

        vowels = 'aeiouAEIOU'

        while lw < hg:
            
            if s[lw] not in vowels: 
                lw += 1

            if s[hg] not in vowels:
                hg -= 1
                
            if s[lw]  in vowels and s[hg]  in vowels:
                temp = s[lw]
                s[lw] = s[hg]
                s[hg] = temp
                lw += 1
                hg -= 1


        return "".join(s)
            
                
                
        