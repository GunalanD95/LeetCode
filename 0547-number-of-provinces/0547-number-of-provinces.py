from collections import deque
class Solution:
    def bfs(self,src,adj,visited):
        q = deque()
        q.append(src)
        visited[src] = True
        
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                nodes    = len(adj[cur_node])
                
                for child in range(nodes):
                    if not visited[adj[cur_node][child]]:
                        q.append(adj[cur_node][child])
                        visited[adj[cur_node][child]] = True

    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N =  len(isConnected)
        
        check = True
        adj = [[] for _ in range(N+1)]
        for i in range(N):
            for j in range(N):
                if i != j and isConnected[i][j] == 1:
                    check = False
                    row = i + 1
                    val = j + 1
                    adj[row].append(val)
                    
        if check:
            return N
                    
                    
        visited = [False] * (N+1)
        
        count   = 0
        for node in range(1,N+1):
            if not visited[node]:
                self.bfs(node,adj,visited)
                count += 1
                
        return count

        
        