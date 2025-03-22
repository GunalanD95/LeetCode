from collections import defaultdict
class Solution:
    def bfs(self, src):
        q = deque()
        q.append(src)
        nodes = []
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_node in self.visited:
                    continue
                self.visited.add(cur_node)
                nodes.append(cur_node)
                for child in self.graph[cur_node]:
                    if child not in self.visited:
                        q.append(child)

        print("NODES",nodes)
        return nodes

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph = defaultdict(set)
        self.visited = set()
        for u,v in edges:
            self.graph[u].add(v)
            self.graph[v].add(u)

        print("graph",self.graph)
        components = []
        for node in range(n):
            if node not in self.visited:
                components.append(self.bfs(node))

        count = 0
        for nodes in components:
            connected = True
            for i in range(len(nodes)):
                for j in range(i+1,len(nodes)):
                    u = nodes[i]
                    v = nodes[j]
                    print(u,self.graph[v],v)
                    if u not in self.graph[v]:
                        connected = False
                        break

            if connected:
                count += 1
        return count    