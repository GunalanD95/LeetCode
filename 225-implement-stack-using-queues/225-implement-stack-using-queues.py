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
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()