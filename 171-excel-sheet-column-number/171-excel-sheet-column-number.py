class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = len(columnTitle) - 1
        
        powal = 0
        ans = 0
        while s >= 0:
            val = ord(columnTitle[s]) - 64
            ans += val * (26**powal)
            powal += 1
            s -= 1
        return ans
        