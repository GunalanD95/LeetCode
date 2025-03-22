from collections import defaultdict
class Solution:
    def bfs(self, src):
        q = deque()
        q.append(src)
        self.visited.add(src)
        size = 0
        edges_count = 0
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                size += 1
                edges_count += len(self.graph[cur_node])
                for child in self.graph[cur_node]:
                    if child not in self.visited:
                        q.append(child)
                        self.visited.add(child)
        edges_count //= 2
        check = size * (size -1)//2
        return check == edges_count

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph = defaultdict(set)
        self.visited = set()
        for u,v in edges:
            self.graph[u].add(v)
            self.graph[v].add(u)
        count = 0
        for node in range(n):
            if node not in self.visited:
                if self.bfs(node):
                    count += 1
        return count    