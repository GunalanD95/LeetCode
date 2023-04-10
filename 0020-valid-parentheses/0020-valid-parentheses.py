class MyStack:

    def __init__(self):
        self.stk = []
        

    def push(self, x: int) -> None:
        self.stk.append(x)
        

    def pop(self) -> int:
        if not self.empty():
            return self.stk.pop()

    def top(self) -> int:
        if not self.empty():
            return self.stk[-1]
        

    def empty(self) -> bool:
        if len(self.stk) !=0:
            return False
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        ll = MyStack()
        l = '([{'
        r = '])}'
        
        for i in range(len(s)):
            if s[i] in l:
                ll.push(s[i])

            elif s[i] in r:
                if len(ll.stk) == 0:
                    return False
                
                top = ll.top()
                if top == '(' and s[i] == ')':
                    ll.pop()
                    
                elif top == '[' and s[i] == ']':
                    ll.pop()
                    
                elif top == '{' and s[i] == '}':
                    ll.pop()
                    
                else:
                    return False
                    
                    
        if len(ll.stk) != 0:
            return False
        
        return True
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                