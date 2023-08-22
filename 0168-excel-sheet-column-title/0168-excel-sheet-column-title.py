class Solution:
    def convertToTitle(self, columnNumber: int) -> str:        
        res = []
        
        while columnNumber > 0:
            digit = columnNumber % 26
            columnNumber = columnNumber // 26
            if digit == 0:
                digit = 26
                columnNumber -= 1
            string_val   = chr(digit+ord('A')-1)
            res.append(string_val)
            
        return "".join(res[::-1])