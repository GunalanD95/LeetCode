class DisjoinSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n  

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a == parent_b:
            return False  

        if self.rank[parent_a] > self.rank[parent_b]:
            self.parent[parent_b] = parent_a
        elif self.rank[parent_a] < self.rank[parent_b]:
            self.parent[parent_a] = parent_b
        else:
            self.parent[parent_b] = parent_a
            self.rank[parent_a] += 1

        return True

        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        graph = defaultdict(list)
        dsu   = DisjoinSet(n)
        
        for u,v in edges:
            if not dsu.union(u,v):
                return False
        
        return True