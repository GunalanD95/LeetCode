from collections import deque

class Solution:
    def _bfs(self,src,des):
        q = deque()
        q.append(src)
        
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_node in self.visited:
                    continue
                
                if cur_node == des:
                    return True
                    
                self.visited.add(cur_node)
                
                for child in self.graph[cur_node]:
                    if child not in self.visited:
                        q.append(child)
                    
            
            
        return False
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.graph = defaultdict(list)
        for u,v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
            
        self.visited = set()
        return self._bfs(source,destination)