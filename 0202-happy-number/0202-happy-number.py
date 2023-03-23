class Solution:
    def SqrSum(self,num):
        total_sum = 0
        while num > 0:
            last_digit = num % 10 
            total_sum  += last_digit * last_digit
            num = num // 10
        return total_sum
      
    def isHappy(self, num: int) -> bool:
        flag = False
        if num == 0:
            return flag
        if num == 1:
            return True
        seen = set()
        while num > 1:
            num = self.SqrSum(num)
            if num == 1:
                return True
            if num in seen:
                flag = False
                break
            else:
                seen.add(num)
        return flag
      