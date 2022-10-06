class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == 'C':
                stack.pop()

            elif i == 'D':
                top = int(stack[-1])
                stack.append(2 * top)

            elif i == '+':
                val1 = int(stack[-1])
                val2 = int(stack[-2])
                stack.append(val1 + val2)

            else:
                 stack.append(int(i))



        return sum(stack)       