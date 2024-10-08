class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        right_count = 0
        
        swaps = 0
        for char in s:
            if char == '[':
                left += 1
            else:
                right_count += 1
                
                while right_count > left:
                    swaps += 1
                    left += 1
                    right_count -= 1
                        
        return swaps