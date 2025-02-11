class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        k = len(part)
        
        for char in s:
            stack.append(char)

            if len(stack) >= k and self._check_match(stack,part,k):
                for _ in range(k):
                    stack.pop()

        return "".join(stack)
    

    def _check_match(self, stack: list,part: str, part_length: int) -> bool:
        return "".join(stack[-part_length:]) == part