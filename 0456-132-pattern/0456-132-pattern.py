class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []
        second_max = float('-inf')
        
        for num in reversed(nums):
            if num < second_max:
                return True
            while stack and stack[-1] < num:
                second_max = stack.pop()
            stack.append(num)
        
        return False