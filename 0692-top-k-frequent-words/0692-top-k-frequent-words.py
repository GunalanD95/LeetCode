from collections import Counter
import heapq as hq

class HeapItem:
    def __init__(self, word : str, count : int) -> None:
        self.count = count
        self.word  = word
        
    def __lt__(self,to_compare) -> bool:
        if self.count == to_compare.count:
            return self.word > to_compare.word
        
        return self.count < to_compare.count
    
    
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        
        min_heap = []
        for word,count in counter.items():
            heap_item = HeapItem(word,count)
        
            if len(min_heap) < k:
                hq.heappush(min_heap, heap_item)
                
            else:
                if heap_item > min_heap[0] :
                    hq.heappop(min_heap)
                    hq.heappush(min_heap,heap_item)
        
        res = []
        while k:
            cur = hq.heappop(min_heap)
            res.append(cur.word)
            k -= 1
        return res[::-1]
        