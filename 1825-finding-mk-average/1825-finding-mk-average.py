from sortedcontainers import SortedList
class SortedListSum:
    def __init__(self):
        self.sl = SortedList()
        self.total = 0 
        
    def add(self,num):
        self.sl.add(num)
        self.total += num
    
    def remove(self,num):
        self.sl.remove(num)
        self.total -= num

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m , self.k = m , k
        self.low  = SortedListSum()
        self.mid   = SortedListSum()
        self.high = SortedListSum()
        self.q = deque()        
        

    def addElement(self, num: int) -> None:
        if not self.low.sl or num <= self.low.sl[-1]:
            self.low.add(num)
        elif not self.high.sl or num >= self.high.sl[0]:
            self.high.add(num)
        else:
            self.mid.add(num)
            
        # Add the new element to the end of the window deque.
        self.q.append(num)
        if len(self.q) > self.m:
            last_ele = self.q.popleft()
            if last_ele in self.low.sl:
                self.low.remove(last_ele)
            elif last_ele in self.high.sl:
                self.high.remove(last_ele)
            else:
                self.mid.remove(last_ele)
                
        self.rebalance_lists()
        
    def rebalance_lists(self):
        # Ensure that low and high always have exactly 'k' elements by moving them to and from middle.
        while len(self.low.sl) > self.k:
            last_ele = self.low.sl.pop()
            self.mid.add(last_ele)

        while len(self.high.sl) > self.k:
            last_ele = self.high.sl.pop(0)
            self.mid.add(last_ele)
        
        while len(self.low.sl) < self.k and self.mid.sl:
            last_ele = self.mid.sl.pop(0)
            self.mid.total -= last_ele
            self.low.add(last_ele)
            
        while len(self.high.sl) < self.k and self.mid.sl:
            last_ele = self.mid.sl.pop()
            self.mid.total -= last_ele
            self.high.add(last_ele) 
        

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        
        return self.mid.total // (self.m - 2 * self.k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()