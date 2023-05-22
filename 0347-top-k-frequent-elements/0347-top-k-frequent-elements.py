import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap  = Counter(nums)
        max_heap = []
        ans      = []
        
        
        for num in freqMap:
            hq.heappush(max_heap,(-freqMap[num],num))
            
            
        while k > 0 and max_heap:
            _ , val  = hq.heappop(max_heap)
            ans.append(val)
            k -= 1
            
        return ans 