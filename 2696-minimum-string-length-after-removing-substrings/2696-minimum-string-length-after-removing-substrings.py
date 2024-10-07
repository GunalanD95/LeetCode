from collections import deque

class Solution:
    def minLength(self, s: str) -> int:
        N = len(s)
        stack = []
        for idx in range(N):
            char = s[idx]            
            stack.append(char)
            if len(stack) >= 2:
                while len(stack) >= 2 and (stack[-2] + stack[-1] == 'AB' or stack[-2] + stack[-1] == 'CD'):
                    stack.pop()
                    stack.pop()
                
        return len(stack)