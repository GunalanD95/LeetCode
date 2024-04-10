import heapq as hq

class Solution:
    def config(self, arr, adj, in_degree, min_heap):
        for preq_c, next_c in arr:
            adj[preq_c].append(next_c)
            in_degree[next_c] += 1

        for course in range(1, len(in_degree)):
            if in_degree[course] == 0:
                hq.heappush(min_heap, (0, course))

    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        in_degree = [0] * (n + 1)
        min_heap = []

        self.config(relations, adj, in_degree, min_heap)

        topo_ans = []
        res = 0  # Change here: initialize res as 0
        while min_heap:
            res += 1  # Change here: increment res for each semester
            next_sem_courses = []
            while min_heap:
                _, cur_node = hq.heappop(min_heap)
                topo_ans.append(cur_node)

                for child in adj[cur_node]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        next_sem_courses.append(child)

            for course in next_sem_courses:
                hq.heappush(min_heap, (0, course))

        if len(topo_ans) != n:
            return -1

        return res
