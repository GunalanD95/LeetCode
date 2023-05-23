import heapq as hq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        hq.heapify(self.minheap)
        self.k       = k
        
        
    def insert(self, val: int):
        hq.heappush(self.minheap,val) # push current element in the minheap
        
        # remove all elements from front (smaller)
        while len(self.minheap) > self.k:
            hq.heappop(self.minheap)
        

    def add(self, val: int) -> int:
        self.insert(val)
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)