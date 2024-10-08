class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        
        for char in s:
            if char == '[':
                count += 1
            else:
                if count > 0:
                    count -= 1
                    
                    
        return (count + 1)//2