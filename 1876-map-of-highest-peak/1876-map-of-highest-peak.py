from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # 1 -> WATER , 0 -> LAND
        # ASSIGN ALL LANDS A HEIGHT (+VE)
        # MAX HEIGHT IS MAXIMIED
        rows, cols = len(isWater) , len(isWater[0])
        q = deque() # (value,row,col)
        output = [[None]*cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if isWater[row][col] == 1:
                    q.append((0,row,col))
                    output[row][col] = 0
        
        def out_of_bound(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return True
            return False

        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        while q:
            for _ in range(len(q)):
                val , cr , cc = q.popleft()
                for r,c in directions:
                    nr , nc = cr + r , cc + c
                    if out_of_bound(nr,nc) or output[nr][nc] != None:
                        continue
                    output[nr][nc] = val + 1
                    q.append((val+1,nr,nc))
        return output