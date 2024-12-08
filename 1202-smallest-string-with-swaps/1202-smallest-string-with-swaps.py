from collections import defaultdict

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a != parent_b:
            self.parent[parent_b] = parent_a  # Attach parent_b to parent_a   

        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        dsu = DisjointSet(N)

        for u,v in pairs:
            dsu.union(u,v)
        
        components = defaultdict(list)
        
        for node in range(N):
            parent = dsu.find(node)
            components[parent].append(node)
            
        result = list(s)
        
        # Sort characters within each component
        for indices in components.values():
            # Extract the characters, sort them, and place them back in the result
            characters = [s[i] for i in indices]
            characters.sort()
            for i, idx in enumerate(sorted(indices)):
                result[idx] = characters[i]
        
        return "".join(result)