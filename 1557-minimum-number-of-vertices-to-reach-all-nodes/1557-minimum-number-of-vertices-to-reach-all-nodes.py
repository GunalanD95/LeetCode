class Solution:

    
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj =  [[] for _ in range(n)]
        
        indeg = [0] * n
        
        for u , v in edges:
            adj[u].append(v)
            indeg[v] += 1
            
        ans = []
        
        for node in range(n):
            if indeg[node] == 0:
                ans.append(node)
        
        return ans
            
            
        
            
        
        