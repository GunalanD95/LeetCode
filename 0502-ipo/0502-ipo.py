import heapq as hq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        minCapital = [[c,p] for c,p in zip(capital,profits)]
        hq.heapify(minCapital)
        maxProfits = []
        
        
        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c , p = hq.heappop(minCapital)
                hq.heappush(maxProfits,-p)
            
            if not maxProfits: break
            w += -hq.heappop(maxProfits)
            
            
        return w
        