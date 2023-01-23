from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [0] * (n+1)
        
        
        for u , v in trust:
            adj[u] -= 1
            adj[v] += 1
            
        
        for i in range(1,n+1):
            if adj[i] == n-1:
                return i
            
            
        return -1
        