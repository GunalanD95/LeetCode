class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        st = len(s) - 1
        res = ''

        while st >= 0:
            if not stack:
                stack.append(1)
            if stack[-1] == -1 and s[st] != '*':
                stack.pop(-1)

            elif stack[-1] == 1 and s[st] != '*':
                res = s[st] +  res 

            if s[st] == '*':
                stack.append(-1)        

            st -= 1  
            
        return res