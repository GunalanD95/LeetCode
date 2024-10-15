import heapq as hq

class Solution:
    def getSuperParent(self,node,Parent):
        if node == Parent[node]:
            return node
        Parent[node] = self.getSuperParent(Parent[node],Parent)
        return Parent[node]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N+1)]
        ans  = None
        for u,v in edges:
            uParent = self.getSuperParent(u,parent)
            vParent = self.getSuperParent(v,parent)

            if uParent != vParent:
                parent[max(uParent,vParent)] = parent[min(uParent,vParent)]
            else:
                ans = [u,v]
        return ans