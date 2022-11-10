import heapq as hq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])        
        minheap = []
        for i in range(row):
            for j in range(col):
                hq.heappush(minheap, matrix[i][j])
                        
        for _ in range(k-1):   # need kth ele so remove all min values < k
            hq.heappop(minheap)
        return(minheap[0])
        