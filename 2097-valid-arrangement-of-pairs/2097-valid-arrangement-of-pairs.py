from collections import defaultdict
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Build graph and track degrees
        graph = defaultdict(list)
        out_degree = defaultdict(int)
        in_degree = defaultdict(int)
        
        # Track all unique nodes
        nodes = set()
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
            nodes.add(start)
            nodes.add(end)
        
        # Find potential start node
        start_node = pairs[0][0]
        for node in nodes:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
        
        # Iterative Hierholzer's algorithm
        def find_eulerian_path(start):
            path = []
            stack = [start]
            
            while stack:
                current = stack[-1]
                
                # If no more outgoing edges, add to path and pop
                if not graph[current]:
                    path.append(current)
                    stack.pop()
                else:
                    # Take the first available edge
                    next_node = graph[current].pop(0)
                    stack.append(next_node)
            
            return path[::-1]
        
        # Find the Eulerian path
        path = find_eulerian_path(start_node)
        
        # Convert path to pairs
        return [[path[i], path[i+1]] for i in range(len(path)-1)]