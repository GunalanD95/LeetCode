class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        total_sum = 0
        temp = x
        x = abs(x)
        
        while x > 0:
            last_digit = x % 10
            
            total_sum *= 10
            total_sum += last_digit
        
            x = x // 10
        
        return total_sum == temp
        
        
        