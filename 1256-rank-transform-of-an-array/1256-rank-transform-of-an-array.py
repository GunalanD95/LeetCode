import heapq as hq
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        N = len(arr)
        out_put = [None] * N
        
        min_heap = []
        for idx,num in enumerate(arr):
            hq.heappush(min_heap,(num,idx))
        
        rank = 0
        prv  = None
        while min_heap:
            cur , index = hq.heappop(min_heap)
            if cur != prv:
                rank += 1
            prv =  cur
            
            out_put[index] = rank
        return out_put