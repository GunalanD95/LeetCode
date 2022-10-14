from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.stack = []
        self.hmap1 = {}
        self.hmap2 = defaultdict(list)
        self.maxcount = 0
        

    def push(self, val: int) -> None:
        if val not in self.hmap1:
            self.hmap1[val]  = 1
        else:
            self.hmap1[val] += 1

        self.maxcount = max(self.maxcount,self.hmap1[val])
        self.hmap2[self.hmap1[val]].append(val)
        
        
            
    def pop(self) -> int:
        count = self.maxcount
        if self.hmap2[self.maxcount]:
            ele = self.hmap2[self.maxcount].pop()
            self.hmap1[ele] -= 1
            
        if not self.hmap2[self.maxcount]:
            self.maxcount -= 1
        
          
        return ele                     
                
                
                
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()