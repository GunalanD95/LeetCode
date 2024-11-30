class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        one = 0
        two = 1
        three = 1
        
        cur_sum = 0
        for i in range(3,n+1):
            cur_sum = one + two + three
            one = two
            two = three
            three = cur_sum
            
        return cur_sum