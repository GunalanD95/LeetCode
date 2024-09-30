class CustomStack:

    def __init__(self, maxSize: int):
        self._stack = [0] * maxSize
        self._inc   = [0] * maxSize
        
        self._top   = -1
        

    def push(self, x: int) -> None:
        if self._top < len(self._stack) - 1:
            self._top += 1
            self._stack[self._top] = x

    def pop(self) -> int:
        if self._top < 0:
            return -1
        
        val = self._stack[self._top] + self._inc[self._top]
        
        if self._top > 0:
            self._inc[self._top -1] += self._inc[self._top]
        
        self._inc[self._top] = 0
        self._top -= 1
        return val
    
         

    def increment(self, k: int, val: int) -> None:
        if self._top >= 0:
            index = min(self._top , k -1)
            self._inc[index] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)