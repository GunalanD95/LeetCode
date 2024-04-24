class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" is num1 or "0" is num2:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        
        pos = len(res) - 1
        
        for i1 in num1[::-1]:
            tempPos = pos
            for i2 in num2[::-1]:
                res[tempPos] += int(i1) * int(i2)
                res[tempPos-1] += res[tempPos]//10
                res[tempPos] %= 10
                tempPos -= 1
            pos -= 1
            
        
        pt = 0
        while pt < len(res) and res[pt] == 0:
            pt += 1
            
        return "".join(map(str,res[pt:]))
        
            
        