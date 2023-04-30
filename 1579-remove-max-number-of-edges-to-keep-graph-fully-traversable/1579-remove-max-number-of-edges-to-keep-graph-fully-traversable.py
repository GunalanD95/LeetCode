class DSU:
    
    def  __init__(self,n):
        self.parents = list(range(n))
        self.edges   = 0
        
    def Find(self,node):
        if node == self.parents[node]:
            return node
        
        self.parents[node] = self.Find(self.parents[node])
        return self.parents[node]
        
    def Union(self,x,y):
        Parent1 = self.Find(x)
        Parent2 = self.Find(y)

        if Parent1 != Parent2:
            self.parents[Parent2] = Parent1
            self.edges     += 1
            return 0
        else:
            return 1
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n+1)
        bob   = DSU(n+1)
        
        ans   = 0
        
        for t , u , v in edges:
            if t == 3:
                ans += alice.Union(u,v)
                bob.Union(u,v)
            
        # construct MST for type-1 edges
        for t , u , v in edges:
            if t == 1:
                ans += alice.Union(u,v)
                
        # check if there is only one connected component
        if alice.edges != n-1:
            return -1
        
        # construct MST for type-2 edges
        for t , u , v in edges:
            if t == 2:
                ans += bob.Union(u,v)
                
        # check if there is only one connected component
        if bob.edges != n-1:
            return -1
        
        return ans

