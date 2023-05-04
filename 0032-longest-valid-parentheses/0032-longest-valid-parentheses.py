from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        
        N = len(s)
        max_len , cur_len  = 0 , 0
        for i in range(N):
            char = s[i]
            
            if char == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    cur_len = i - stack[-1]
                    max_len = max(max_len,cur_len)
            
        return max_len
        