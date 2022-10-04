class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) == 1: return s
        
        stack = [['#',-1]]


        for i in range(len(s)):
            top = stack[-1]
            if top[0] != s[i]:
                cur = [s[i],1]
                stack.append(cur)
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        ans = ''
        for j in range(1,len(stack)):
            count = stack[j][1]
            while count != 0:
                ans += stack[j][0]
                count -= 1
        
        return ans 