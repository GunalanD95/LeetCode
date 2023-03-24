class Solution:
    def bfs(self):
        q = deque()
        q.append(0)
        self.visited[0] =  True
        while q:
            cur_node = q.popleft()
            for child  in self.adj[cur_node]:
                if not self.visited[child]:
                    if (child,cur_node) not in self.seen:
                        self.count += 1
                    q.append(child)
                    self.visited[child] = True 

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.seen = set()
        self.adj  = [[] for _ in range(n)]
        self.visited = [False] * (n)
        
        for u , v in connections:
            self.seen.add((u,v))
            self.adj[u].append(v)
            self.adj[v].append(u)
        
        self.count = 0
        self.bfs()
        return self.count