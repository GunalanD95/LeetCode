from collections import defaultdict
from typing import List

class Solution:
    def dfs(self, node, parent, graph, heights):
        longest, second_longest = 0, 0  # Longest and second-longest heights
        
        for child in graph[node]:
            if child == parent: 
                continue
            child_height = self.dfs(child, node, graph, heights)
            
            if child_height > longest:
                second_longest = longest
                longest = child_height
            elif child_height > second_longest:
                second_longest = child_height
        
        # Store the height of the current node
        heights[node] = longest
        # Update the global diameter
        self.global_diameter = max(self.global_diameter, longest + second_longest)
        
        # Return the height of the current subtree
        return longest + 1

    def find_heights_and_diameter(self, edges, n):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        heights = [0] * n  # Store the height of each node
        self.global_diameter = 0
        self.dfs(0, -1, graph, heights)  # Perform DFS from node 0
        return self.global_diameter, heights

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Number of nodes in the two trees
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        
        # Find diameters and heights for both trees
        diameter1, heights1 = self.find_heights_and_diameter(edges1, n1)
        diameter2, heights2 = self.find_heights_and_diameter(edges2, n2)
        
        # Check all possible connections between the two trees
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum of the three possibilities
        return max(diameter1, diameter2, combined_diameter)
