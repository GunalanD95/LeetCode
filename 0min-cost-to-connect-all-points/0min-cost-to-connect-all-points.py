import heapq as hq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        min_heap = [(0, 0)]  # (cost, starting point)
        total_cost = 0
        seen = set()
        edges_used = 0  # To track number of edges added to MST

        while len(seen) < N:
            cost, curr = hq.heappop(min_heap)
            
            # If the node is already seen, skip it
            if curr in seen:
                continue
            
            # Add node to the MST
            seen.add(curr)
            total_cost += cost
            edges_used += 1

            # Add all edges from the current node to the heap
            for next_node in range(N):
                if next_node not in seen:
                    x1, y1 = points[curr]
                    x2, y2 = points[next_node]
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    hq.heappush(min_heap, (distance, next_node))

        return total_cost
