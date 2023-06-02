class Solution:
    def topo_sort(self, graph, n):
        
        topo = []
        
        def dfs(node):
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
                    
            topo.append(node)
            
        seen = set()
        
        for node in range(n):
            if node not in seen:
                seen.add(node)
                dfs(node)
                
        return topo[::-1]
        
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        
        for u, (x1, y1, r1) in enumerate(bombs):
            for v, (x2, y2, r2) in enumerate(bombs):
                if u == v:
                    continue
                    
                if (x2 - x1)**2 + (y2 - y1)**2 <= r2**2:
                    graph[v].add(u)
                    
        def dfs(bomb, vis):
            for nbomb in graph[bomb]:
                if nbomb not in vis:
                    vis.add(nbomb)
                    dfs(nbomb, vis)
            
        seen = set()
        ans = 0
        for bomb in self.topo_sort(graph, len(bombs)):
            if bomb not in seen:
                vis = set()
                vis.add(bomb)
                dfs(bomb, vis)
            
            ans = max(ans, len(vis))
            seen |= vis
            
        return ans