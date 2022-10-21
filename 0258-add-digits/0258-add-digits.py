class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        
        last_digit = num % 10
        rem        = num //10
        return self.addDigits(last_digit + rem)
