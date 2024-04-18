class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoded_arr = encoding
        self.remaining   = len(encoding)
        self.cur_idx     = 0
                
    def next(self, n: int) -> int:
        
        while self.cur_idx < len(self.encoded_arr) and n > self.encoded_arr[self.cur_idx]:
            n -= self.encoded_arr[self.cur_idx]
            self.cur_idx += 2
            
        if self.cur_idx >= len(self.encoded_arr):
            return -1
            
        self.encoded_arr[self.cur_idx] -= n
        self.remaining -= n    
        
        return self.encoded_arr[self.cur_idx+1]
        
        
        
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)