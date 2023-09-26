class Solution:
    def removeDuplicateLetters(self, s: str) -> str:        
        seen  = set()
        stack = []
        counter = Counter(s)
        
        
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                seen.add(s[i])
                counter[s[i]] -= 1
            else:
                cur_char = ord(s[i])
                
                if s[i] in seen:
                    counter[s[i]] -= 1
                    continue
                    
                while stack and ord(stack[-1]) >= cur_char and counter[stack[-1]] > 0:
                    seen.remove(stack[-1])
                    stack.pop()

                stack.append(s[i])
                seen.add(s[i])
                counter[s[i]] -= 1
                
        return ''.join(stack)
                
                
        
        