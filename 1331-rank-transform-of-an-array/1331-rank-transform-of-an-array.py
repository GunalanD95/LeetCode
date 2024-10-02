from collections import defaultdict
import heapq as hq

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        N = len(arr)
        
        rankMap = defaultdict(int)
        temp  = arr[:]
        hq.heapify(arr)
        
        rank = 0
        prev = None
        
        while  arr:
            num = hq.heappop(arr)
            if prev != num:
                rank += 1
            rankMap[num] = rank
            prev = num
            
        out = []
        
        for num in temp:
            out.append(rankMap[num])
        
        return out