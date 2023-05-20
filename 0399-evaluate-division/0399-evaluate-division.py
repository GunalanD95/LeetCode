from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        N = len(equations)

        for idx in range(N):
            dividend, divisor = equations[idx]
            value = values[idx]
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        def dfs(dividend: str, divisor: str, visited: set) -> float:
            if dividend not in graph or divisor not in graph:
                return -1.0
            if dividend == divisor:
                return 1.0
            if divisor in graph[dividend]:
                return graph[dividend][divisor]

            visited.add(dividend)
            for neighbor in graph[dividend]:
                if neighbor not in visited:
                    result = dfs(neighbor, divisor, visited)
                    if result != -1.0:
                        return result * graph[dividend][neighbor]

            return -1.0

        result = []
        for dividend, divisor in queries:
            visited = set()
            result.append(dfs(dividend, divisor, visited))

        return result
