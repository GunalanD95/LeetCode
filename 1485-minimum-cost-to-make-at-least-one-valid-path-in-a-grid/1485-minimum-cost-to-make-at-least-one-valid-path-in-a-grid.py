import heapq as hq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        N , M = len(grid) , len(grid[0])
        mapper = {
            1: (0,1),
            2: (0,-1),
            3: (1,0),
            4: (-1,0)
        }

        def check_out_bound(i,j ):
            if i < 0 or j < 0 or i >= N or j >= M or (i,j) in visited:
                return True
            return False

        min_heap = [(0, 0, 0)] 
        visited = set()

        while min_heap:
            cur_cost, i, j = hq.heappop(min_heap)

            if check_out_bound(i, j):
                continue

            if i == N-1 and j == M-1:
                return cur_cost

            visited.add((i,j))

            r , c = mapper[grid[i][j]]
            new_r,new_c = i + r , j +  c
            if not check_out_bound(new_r,new_c):
                hq.heappush(min_heap,(cur_cost,new_r,new_c))   

            for direction in range(1,5):
                r , c = mapper[direction]
                new_r,new_c = i + r , j +  c
                if not check_out_bound(new_r,new_c):
                    hq.heappush(min_heap,(cur_cost+1,new_r,new_c))  


        return 0


            

        
