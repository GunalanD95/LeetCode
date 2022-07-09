class stack:
    def __init__(self):
        self.stk = []
    def push(self,val):
        self.stk.append(val)
    def pop(self):
        if not self.isEmpty():
            return self.stk.pop()
    def top(self):
        if not self.isEmpty():
            return self.stk[-1]
    def addback(self,val):
        return self.stk.insert(0,val)
       
    def isEmpty(self):
        if len(self.stk) == 0:
            return True
           
    def getstack(self):
        return self.stk


class Solution:
    def isValid(self, s: str) -> bool:
        ll = stack()

        l = '{(['
        r = '])}'

        ll = stack()

        for i in range(len(s)):
            if s[i] in l:
                ll.push(s[i])

            elif s[i] in r:
                if len(ll.stk) == 0:
                    return False

                top = ll.top()
                if top == '{' and s[i] == '}':
                    ll.pop()

                elif top== '(' and s[i] == ')':
                    ll.pop()
                
                elif top == '[' and s[i] == ']':
                    ll.pop()

                else:
                    return False

        if len(ll.stk) > 0:
            return False

        return True
        