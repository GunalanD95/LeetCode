import heapq as hq

class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        cur_val = num 
        
        diff = abs(len(self.minheap)) - abs(len(self.maxheap))
        
        if diff == 0:
            # cur_val is  greater thann 2 half starting 
            # if any val in coming > min val of second half 
            if self.minheap and  cur_val > self.minheap[0]:
                min_val = hq.heappop(self.minheap)
                hq.heappush(self.minheap,cur_val)
                hq.heappush(self.maxheap,-min_val)
            else:
                hq.heappush(self.maxheap,-cur_val) 
        else:
            if cur_val < -self.maxheap[0]:
                max_val = hq.heappop(self.maxheap)
                hq.heappush(self.minheap,-max_val)
                hq.heappush(self.maxheap,-cur_val)
            else:
                hq.heappush(self.minheap,cur_val)
                


    def findMedian(self) -> float:
        N  = len(self.minheap) + len(self.maxheap)
        # check odd or even
        if not N & 1:
            max_val = -self.maxheap[0] 
            min_val =  self.minheap[0]
            total   = max_val + min_val 
            return float(total/2)
        else:
            return -self.maxheap[0]        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()