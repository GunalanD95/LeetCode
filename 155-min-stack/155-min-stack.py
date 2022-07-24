class MinStack:

    def __init__(self):
        self.stk = []
        self.mnstk = []
        

    def push(self, val: int) -> None:
        if len(self.stk) == 0:
            self.stk.append(val)
            self.mnstk.append(val)
        else:
            self.stk.append(val)
            if val <= self.mnstk[-1]:
                self.mnstk.append(val)
            

    def pop(self) -> None:
        if len(self.stk) == 0:
            return 
        else:
            val = self.stk.pop()
            if val == self.mnstk[-1]:
                self.mnstk.pop()
        

    def top(self) -> int:
        if len(self.stk) !=0:
            return self.stk[-1]
        return -1
        

    def getMin(self) -> int:
        if len(self.mnstk) !=0:
            return self.mnstk[-1]
        return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()