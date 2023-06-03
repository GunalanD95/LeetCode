class Solution:
    def dfs(self, src, adj_list, informTime):
        max_time = 0
        for employee, histm in adj_list[src]:
            max_time = max(max_time, self.dfs(employee, adj_list, informTime) + histm)
        return max_time

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v in enumerate(manager):
            if v != -1:
                adj_list[v].append((u, informTime[u]))
        return self.dfs(headID, adj_list, informTime) + informTime[headID]