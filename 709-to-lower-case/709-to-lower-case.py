class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            val = ord(s[i])
            if val >= 65 and val <= 90:
                newVal = ord(s[i]) + 32
                s[i] = chr(newVal)
                
        return "".join(s)