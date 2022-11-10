import heapq as hq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        min_heap = []
        N = len(arr)
        for i in range(N-1):
            hq.heappush(min_heap, [(arr[i] / arr[-1]), i, N- 1])
            
            
        print("min_heap",min_heap)
        while k - 1:
            _ , i , j = hq.heappop(min_heap)
            
            if  i < j - 1:
                hq.heappush(min_heap, [(arr[i] / arr[j - 1]), i, j -1])
            
            
            k -= 1
            
        return arr[min_heap[0][1]] , arr[min_heap[0][2]]
        