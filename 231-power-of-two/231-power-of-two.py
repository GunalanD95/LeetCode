class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 0: return False
        
        k = n
        while k != 1:
            if k % 2 != 0:
                return False
            k = k // 2
            
            
        return True