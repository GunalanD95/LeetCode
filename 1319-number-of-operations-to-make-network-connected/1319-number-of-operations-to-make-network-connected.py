class Solution:
    def dfs(self,node,adj,visited):
        visited[node] = True
        for child in adj[node]:
            if not visited[child]:
                self.dfs(child,adj,visited)
        
        
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1: # this is a edge condi. to connect n components we need min n-1 cables. 
            return -1
        adj_list = [[] for _ in range(n)]
        
        for u,v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
            
        visited = [False] * (n)
        count   = 0
        for node in range(n):
            if not visited[node]:
                self.dfs(node,adj_list,visited)
                count += 1
                

        
        return count - 1 
        