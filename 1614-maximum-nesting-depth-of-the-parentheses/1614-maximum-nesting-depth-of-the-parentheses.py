class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        
        left , right = 0 , 0
        
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                right += 1
            elif char == '*' or char == '+':
                continue
            ans = max(ans,left-right)            
        return ans