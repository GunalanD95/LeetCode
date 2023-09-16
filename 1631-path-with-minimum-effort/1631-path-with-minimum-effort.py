import heapq as hq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        N = len(heights)
        M = len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dist_arr   = [[float('inf')] * (M) for _ in range(N)]
        dist_arr[0][0] = 0
        
        min_heap   = []
        hq.heappush(min_heap,(0,0,0)) # i,j,distance
        
        while min_heap:
            row , col , cur_dis = hq.heappop(min_heap)
            
            if row == N-1 and col == M-1:
                return cur_dis
            
            for r , c in directions:
                nr = row + r
                nc = col + c
                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue
                
                old_val = heights[row][col]
                new_val = heights[nr][nc]
                
                new_dis  = abs(old_val - new_val)
                next_dis = max(new_dis,cur_dis)
                
                if next_dis <  dist_arr[nr][nc]:
                    hq.heappush(min_heap,(nr,nc,next_dis))
                    dist_arr[nr][nc] = next_dis
                    
        return 0
                    
                
            