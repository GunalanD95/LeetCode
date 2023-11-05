from collections import *

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        hmap = defaultdict(int)
        
        q    = deque(arr)
        
        if k >= len(arr):
            return max(arr)        
        
        while q: 
            first_val  = q.popleft()
            second_val = q.popleft()
            min_v , max_v = min(first_val,second_val) , max(first_val,second_val)
            
            q.appendleft(max_v)
            q.append(min_v)

            hmap[max_v] += 1
            
            if hmap[max_v] >= k:
                return max_v
            
            
            
        return -1