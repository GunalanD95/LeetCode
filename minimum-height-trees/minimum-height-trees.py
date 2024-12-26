from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        leaves = deque(node for node in range(n) if len(graph[node]) == 1)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves
            
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)
                        
                del graph[leaf]
                
        return list(leaves)