import heapq as hq

class Solution:
    def getSuperParent(self,node,Parent):
        if node == Parent[node]:
            return node 

        Parent[node] = self.getSuperParent(Parent[node],Parent)

        return Parent[node]
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []
#         |xi - xj| + |yi - yj|
        for idx,(x1,y1) in enumerate(points):
            for jdx,(x2,y2) in enumerate(points):
                if idx == jdx:
                    continue
                val = abs(x1-x2) + abs(y1-y2)
                edges.append((idx,jdx,val))
                
        edges.sort(key=lambda x:x[2])
        
        Parent = [i for i in range(N)] 
        total_cost = 0
        
        for u , v , w in edges:

            uParent = self.getSuperParent(u,Parent)
            vParent = self.getSuperParent(v,Parent)

            if uParent != vParent:
                total_cost += w

                Parent[max(uParent,vParent)] = Parent[min(uParent,vParent)]

        return total_cost