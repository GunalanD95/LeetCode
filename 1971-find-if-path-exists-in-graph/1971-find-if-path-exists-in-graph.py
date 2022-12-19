class Solution:
    def dfs(self,node,des,visited,adj):
        visited[node]      = True 

        for child in adj[node]:
            if not visited[child]:
                if self.dfs(child,des,visited,adj):
                    return True 
            

        return visited[des]
        
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False] * n
        adj     = [[] for _ in range(n)]
        
        for idx in range(len(edges)):
            row = edges[idx][0]
            val = edges[idx][1]
            
            adj[row].append(val)
            adj[val].append(row)
            
        if self.dfs(source,destination,visited,adj):
            return True 
        
        return False
        
            
        
        
        