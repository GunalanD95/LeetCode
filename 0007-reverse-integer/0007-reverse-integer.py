class Solution:
    def reverse(self, num: int) -> int:
        sign = 1
        
        if num < 0:
            sign = -1
        
        self.rev_sum = 0
        def rev(n):
            if n <= 0:
                return 
            
            rem = n % 10
            
            self.rev_sum = (self.rev_sum * 10) + rem
            
            rev(n//10)
        
        
        rev(abs(num))
        
        
        return 0 if self.rev_sum >  (1 << 31) else self.rev_sum * sign
        
        
        