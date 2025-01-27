from collections import defaultdict , deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        indegree = [0] * numCourses
        ans = [False] * numCourses
        if not prerequisites:
            return ans 
        for a,b in prerequisites:
            graph[a].add(b)
            indegree[b] += 1

        q = deque()
        parent_map = defaultdict(int)
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        ordering = []
        reachable = [[False] * numCourses for _ in range(numCourses)] 

        while q:
            cur_node  = q.popleft()
            ordering.append(cur_node)
            for child in graph[cur_node]:
                indegree[child] -= 1
                reachable[cur_node][child] = True # from cur_node to child

                # now if there a path from X to cur_node , then its X to child too
                for path in range(numCourses):
                    if reachable[path][cur_node]:
                        reachable[path][child] = True

                if indegree[child] == 0:
                    q.append(child)

        ans = []
        for parent,child in queries:
            ans.append(reachable[parent][child])
        return ans
        