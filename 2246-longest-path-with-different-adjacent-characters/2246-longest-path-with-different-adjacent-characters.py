class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n    = len(parent)
        adj  = [[] for _ in range(n)]

        for index , value in enumerate(parent):
            if value != -1:
                adj[value].append(index)

        ans = 1
        def dfs(node):
            nonlocal ans

            longest = secondlong = 0
            for child in adj[node]:
                path_length = dfs(child)

                if s[child] != s[node]:
                    if path_length > longest:
                        secondlong  = longest
                        longest     = path_length
                        
                    elif secondlong < path_length:
                        secondlong = path_length

            
            ans = max(ans,longest+secondlong+1)

            return longest+1

        dfs(0)
        return ans
        