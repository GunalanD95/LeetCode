from collections import deque
class Solution:
    def bfs(self,src,graph,visited)-> bool:
        q = deque()
        q.append((src,'red'))
        visited[src] = True
        
        while q:
            nodes = len(q)
            
            for _ in range(nodes):
                cur_node , parent_color = q.popleft()
                for child in graph[cur_node]:
                    # if not visited then mark adjacent nodes to different color 
                    if not visited[child]:
                        # register the current colo
                        if parent_color == 'red':
                            q.append( (child,'black') )
                            visited[child] = 'black'
                        else:
                            q.append( (child,'red') )
                            visited[child] = 'red'
                    else:
                        # that means already visted now check color is same as parent color
                        if parent_color == visited[child]:
                            return False
                        
        return True 
        
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        visited = [False] * (N)
        
        for node in range(N):
            if not visited[node]:
                if not self.bfs(node,graph,visited):
                    return False
                
        return True 
        

                            
                
                
                
                
                
            
        
        
        