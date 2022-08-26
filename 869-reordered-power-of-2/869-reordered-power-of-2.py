from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        c = Counter(str(n))


        for i in range(32):
            mask = 1 << i
            val = Counter(str(mask))
            if c == val:
                return True
            
        return False

        
        
        
        '''
        we just to find a number who is a power of 2 --> 2 , 4 , 8,16,32
        
        using the given number , we can shuffle the given number as per we want 
        
        
        
        '''
        