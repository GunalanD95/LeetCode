class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if char.islower():
                if stack and stack[-1].isupper() and stack[-1].lower() == char:
                    stack.pop()
                    continue
                else:
                    stack.append(char)
            else:
                if stack and stack[-1].islower() and stack[-1].upper() == char:
                    stack.pop()
                    continue
                else:
                    stack.append(char)                
        
        return "".join(stack)
        
        
        