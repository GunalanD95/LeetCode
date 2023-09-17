from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        visited = set((i, 1 << i) for i in range(N))  # default config
        final_state = (1 << N) - 1 # eg: '1111'
        q = deque([(i, 1 << i) for i in range(N)])    # we should try from all nodes with its dc
        steps = 0
        
        while q:
            for _ in range(len(q)):
                cur_node, cur_state = q.popleft()

                if cur_state == final_state:
                    return steps

                for child in graph[cur_node]:
                    # mask to change set bit
                    new_state = cur_state | (1 << child)

                    if (child, new_state) not in visited:
                        visited.add((child, new_state))
                        q.append((child, new_state))
            steps += 1
        return 0

