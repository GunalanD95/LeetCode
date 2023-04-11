class Solution:
    def removeStars(self, s: str) -> str:
        stack = []        
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                if not stack: continue
                stack.pop()
        return "".join(stack)