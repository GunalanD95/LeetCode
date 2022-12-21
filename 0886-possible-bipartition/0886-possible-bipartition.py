from collections import deque 

class Solution:
    def TwoColoring(self,adj,visited,src):
        q = deque()
        q.append((src,'red'))          # node , color 
        visited[src] = 'red'
        # apply 2-coloring
        
        while q:
            node , color = q.popleft()
            
            for child  in adj[node]:
                if not visited[child]:
                    childColor = None
                    if color == 'red':
                        childColor = 'black'
                    else:
                        childColor = 'red'
                    
                    visited[child] = childColor
                    q.append((child,childColor))
                    
                else:
                    if color == visited[child]:
                        return False

        return True 
        
        
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = [False] * (n+1)
        adj     = [[] for _ in range(n+1)]
        
        for idx in range(len(dislikes)):
            row = dislikes[idx][0]
            val = dislikes[idx][1]
            
            adj[row].append(val)
            
            adj[val].append(row)
        
        for node in range(1,n+1):
            if not visited[node] and not self.TwoColoring(adj,visited,node):
                return False
            
        return  True
        