class Solution:
    def clearDigits(self, s: str) -> str:
        N = len(s)
        stack = []

        for indx,char in enumerate(s):
            val = ord(char)
            if val >= 97 and val <= 122:
                stack.append(char)
            else:
                stack.pop()

        return "".join(stack)
        


        