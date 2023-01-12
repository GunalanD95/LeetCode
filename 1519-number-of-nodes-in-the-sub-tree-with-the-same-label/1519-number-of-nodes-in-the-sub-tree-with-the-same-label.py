class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = [[] for _ in range(n)]
        ans = [0] * n

        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node,parent):
            letter = labels[node]
            cnt = Counter(letter)
            for child in adj[node]:
                if child != parent:
                    cnt += dfs(child,node)

            ans[node] = cnt[labels[node]]
            
            return cnt 
        dfs(0,-1)

        return ans 

        