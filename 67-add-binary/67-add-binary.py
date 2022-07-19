class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = ''
        
        a = a[::-1]
        b = b[::-1]
        
        M = len(a)
        N = len(b)
        
        
        tsum = 0
        carry = 0
        for i in range(max(M,N)):
            valA = ord(a[i]) - ord('0') if i < M else 0
            valB = ord(b[i]) - ord('0') if i < N else 0
            
            tsum = valA + valB + carry
            char = str(tsum % 2)
            res = char + res
            carry = tsum // 2
            
            
        if carry:
            res = '1' + res
            
        return res
            
                
            
        