class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+','-','*','/'])
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                operator = tokens[i]
                val1 = int(stack.pop())
                val2 = int(stack.pop())

                if operator =='+':
                    stack.append(val1+val2)
                elif operator =='-':
                    stack.append(val2-val1)
                elif operator =='*':
                    stack.append(val1*val2)
                elif operator =='/':
                    stack.append(int(val2)/(int(val1)))


        return int(stack[0])
