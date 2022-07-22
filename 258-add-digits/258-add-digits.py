class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        
        
        k = num
        while k > 9:
            l = k%10
            r = k//10
            k = l + r
            
        return k
