class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+','-','*','/'}
        stack = []
        for token in tokens:
            
            if token not in operators:
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                
                
                if token == '-':
                    value = (val2 - val1)
                elif token == '+':
                    value = (val2 + val1)
                elif token == '*':
                    value = (val2 * val1)
                else:
                    value = (val2 / val1)
                    
                value = int(value)
                
                stack.append(value)
        return stack[-1]
    
    def calculate(self, s: str) -> int:
        s = s.lstrip().rstrip()
        N = len(s)
        
        operators = []
        postfix   = []
        current_number = 0
        precedence = {'/': 2, '*': 2, '+': 1, '-': 1}
        
        idx = 0
        while idx < N:
            char = s[idx]
            # cases 
            # case:1 -> if char is empty string skip it
            
            # case:2 -> its char is a digit -> form the current number
            if char.isdigit():
                current_number = current_number * 10 + int(char)
                # add the current number to postfix if its last idx or next val is not num
                if idx == N-1 or not s[idx+1].isdigit():
                    postfix.append(str(current_number))
                    current_number = 0 # reset to form next number
            # case:3 -> if char is in operators
            elif char in precedence:
                while operators and operators[-1] in precedence and \
                    precedence[operators[-1]] >= precedence[char]:
                    postfix.append(operators.pop())
                operators.append(char)
            idx += 1
            
        print("<-operators->",operators)
        print("<-postfix->",postfix)
        
        while operators:
            postfix.append(operators.pop()) 
            
        print("ANS",postfix)
            
        return self.evalRPN(postfix)