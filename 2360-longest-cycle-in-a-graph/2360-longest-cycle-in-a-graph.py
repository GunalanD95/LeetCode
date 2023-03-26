class Solution:
    def dfs(self,node,visited,adj,distance,steps):
        visited[node] = True
        for child in adj[node]:
            if not visited[child]:
                distance[child] = steps+1
                self.dfs(child,visited,adj,distance,steps+1)
                distance[child] = 0
            else:
                if distance[child] > 0:
                    self.max_len = max(self.max_len,steps+1 - distance[child])

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        self.max_len = -1
        visited  = [False] * (n)
        adj = [[] for _ in range(n)]
        distance = [0] * (n)
        
        for idx,val in enumerate(edges):
            if val !=-1:
                adj[idx].append(val)
                
        for node in range(n):
            if not visited[node]:
                distance[node] = 1
                self.dfs(node,visited,adj,distance,1)
                distance[node] = 0
        return self.max_len
            
                