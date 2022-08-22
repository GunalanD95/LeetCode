class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        c = 0
        for i in range(32):
            mask = 1 << i
            
            if mask & start:
                v1 = 1
            else:
                v1 = 0
                
            if mask & goal:
                v2 = 1
            else:
                v2 = 0
                
                
            if v1 != v2:
                c += 1
                
                
        return c