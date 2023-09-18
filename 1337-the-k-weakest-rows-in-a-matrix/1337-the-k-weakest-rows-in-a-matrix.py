import heapq as hq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        N , M  = len(mat) , len(mat[0])
        
        min_heap = []
        
        for i in range(N):
            sol_count = 0
            for j in range(M):
                if mat[i][j] == 1:
                    sol_count += 1
                
            hq.heappush(min_heap,(sol_count,i))
            
            
        ans = []
        
        while min_heap and k > 0:
            _ , idx = hq.heappop(min_heap)
            ans.append(idx)
            k -= 1
        return ans