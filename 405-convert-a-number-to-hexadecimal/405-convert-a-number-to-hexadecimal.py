class Solution:
    def toHex(self, num: int) -> str:
        
        if num == 0: return '0'
        
        if num < 0:
            num += 2** 32
            
            
        hexd = '0123456789abcdef'
        
        ans = ''
        while num:
            ans = hexd[num % 16] + ans
            # num = num // 16
            num = num >> 4
            
            
            
        return ans
        