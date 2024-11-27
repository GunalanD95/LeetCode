from collections import defaultdict
class Solution:
    def find_min(self, graph , n , cur_node , dp):
        if cur_node == n-1:
            return 0
        
        if dp[cur_node] != -1:
            return dp[cur_node]
        
        min_distance = n
        
        for nei in graph[cur_node]:
            min_distance = min(min_distance,self.find_min(graph,n,nei,dp)+1)
        
        
        dp[cur_node] = min_distance
        return min_distance
        
        
        
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        dp = [-1] * n  
        
        for idx in range(n-1):
            graph[idx].add(idx+1)
            
        
        res = []
        for u,v in queries:
            graph[u].add(v)
            shortest_path = self.find_min(graph,n,0,dp)
            res.append(shortest_path)
            dp = [-1] * n
        return res