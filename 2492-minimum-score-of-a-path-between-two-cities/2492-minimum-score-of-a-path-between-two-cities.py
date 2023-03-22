from collections import deque
class Solution:
    def bfs(self,src,des,adj,n,visited):
        self.min_weight = float('inf')
        q = deque()
        q.append(src)
        visited[src] =  True
        while q:
            cur_node = q.popleft()
            for child , weight in adj[cur_node]:
                self.min_weight = min(self.min_weight,weight)
                if not visited[child]: 
                    q.append(child)
                    visited[child] = True   
        return visited[des] 
        
        
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj =  [[] for _ in range(n+1)]
        for u , v , w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        visited = [False] * (n+1)
        self.bfs(1,n,adj,n,visited)
        return self.min_weight