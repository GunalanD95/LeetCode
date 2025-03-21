class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        cur  = ''
        for pa  in path + '/':
            if pa == '/':
                if cur == '..':
                    if stack:
                        stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(cur)
                cur = ''
            else:
                cur += pa

        return '/' + '/'.join(stack) 