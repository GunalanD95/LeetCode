import heapq as hq

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:        
        min_heap = []
        N        = len(dist)
        
        for idx in range(N):
            dist_val  = dist[idx]
            speed_val = speed[idx]
            
            time = dist_val / speed_val
            
            hq.heappush(min_heap,time)

        total_monsters = 0
        cur_time = 0

        while min_heap:
            monster_time =  hq.heappop(min_heap)
            
            if monster_time <= cur_time:
                break
                
            total_monsters += 1
            cur_time += 1
            
        return total_monsters
            