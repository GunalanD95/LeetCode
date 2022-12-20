class Solution:
    def dfs(self,node,visited,adj):
        visited[node] = True 

        for child in adj[node]:
            if not visited[child]:
                self.dfs(child,visited,adj)


    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [False] * (N)

        self.dfs(0,visited,rooms)

        return all(visited)      