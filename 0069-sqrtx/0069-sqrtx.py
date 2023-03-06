class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        
        low = 0
        high = x
        
        sqr = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid * mid == x: return mid
            
            if mid * mid <= x: 
                sqr = mid
                low = mid + 1
                
            if mid * mid  > x:
                high = mid - 1
                
                
        return sqr
    
    
    
        '''
        we need to find the largest mid * mid <= N
        '''
            
            
        