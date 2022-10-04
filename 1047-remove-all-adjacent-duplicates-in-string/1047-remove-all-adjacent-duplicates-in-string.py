class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1: return s
        
        
        stack = [s[0]]
        
        for i in range(1,len(s)):
            if stack:
                top = stack[-1]

                if top != s[i]:
                    stack.append(s[i])
                else:
                    stack.pop()
            else:
                stack.append(s[i])

                
                
        return "".join(stack)
        