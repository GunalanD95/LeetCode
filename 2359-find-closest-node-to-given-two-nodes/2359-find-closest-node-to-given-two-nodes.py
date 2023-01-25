class Solution:
    def bfs(self,src,adj,n):
        visited = [False] * n
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque()
        q.append((src,0))
        while q:
            node , dis = q.popleft()
            for child in adj[node]:
                if not visited[child]:
                    q.append((child,dis+1))
                    dist[child] = dis+1
                    visited[node] = True 
        return dist
    
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        adj   = [[] for _ in range(n)]
        for u,v in enumerate(edges):
            if v != -1:
                adj[u].append(v)
        
        dist1 = self.bfs(node1,adj,n)
        dist2 = self.bfs(node2,adj,n)
        
        
        res = float('inf')
        resIdx = -1
        for i, (a, b) in enumerate(zip(dist1, dist2)):
            if max(a, b) < res:
                res = max(a, b)
                resIdx = i
        return resIdx