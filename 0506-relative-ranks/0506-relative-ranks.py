import heapq as hq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = []
        counter  = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal",
        }
        
        for idx,play_score in enumerate(score):
            hq.heappush(max_heap,(-play_score,idx))
            
        ranks = [0] * len(score)
        
        count = 1
        while max_heap:
            _ , idx = hq.heappop(max_heap)            
            if count <= 3:
                ranks[idx] = counter[count]
            else:
                ranks[idx] = str(count)
            count += 1
        return ranks