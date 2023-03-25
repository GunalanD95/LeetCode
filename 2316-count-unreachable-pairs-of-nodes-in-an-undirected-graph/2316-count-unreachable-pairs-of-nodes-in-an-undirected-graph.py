class Solution:
    def bfs(self,src,adj,visited):
        q = deque()
        q.append(src)
        visited[src] = True
        total_nodes = 0
        while q:
            cur_node = q.popleft()
            total_nodes += 1
            for child in adj[cur_node]:
                if not visited[child]:
                    q.append(child)
                    visited[child] = True      
        return total_nodes
        
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False ] * (n)
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        res = 0
        total = n
        for node in range(n):
            if not visited[node]:
                nodes = self.bfs(node,adj,visited)
                rem_nodes   = total - nodes
                value = (nodes * rem_nodes)
                total = rem_nodes
                res   += value
        return res 
        