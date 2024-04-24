class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = ''
        for i in range(0,len(digits)):
             k += str(digits[i])
        k = int(k) + 1
        digits = [int(d) for d in str(k)]

        return digits