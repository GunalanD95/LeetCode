from collections import deque

class Solution:
    def topologicalSorting(self, queue, adj, indegree,colorArray,colors):
        total_nodes = 0

        while queue:
            cur_node = queue.popleft()

            total_nodes += 1

            for child in adj[cur_node]:
                indegree[child] -= 1

                for c in range(26):
                    colorArray[child][c] = max(colorArray[child][c], colorArray[cur_node][c] + (ord(colors[child]) == c + ord('a')))

                if indegree[child] == 0:
                    queue.append(child)

        return total_nodes

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = [[] for _ in range(n)]

        indegree = [0] * (n)

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        queue = deque()

        colorArray = [[0]*26 for _ in range(n)]     # ending at node u (max nodes have color c)

        for node in range(n):
            count = indegree[node]
            if count == 0:
                queue.append(node)
                colorArray[node][ord(colors[node]) - ord('a')] = 1

        total_nodes = self.topologicalSorting(queue, adj, indegree,colorArray,colors)

        if total_nodes != n:
            return -1

        res = 0
        for node in range(n):
            res = max(res, max(colorArray[node]))

        return res
