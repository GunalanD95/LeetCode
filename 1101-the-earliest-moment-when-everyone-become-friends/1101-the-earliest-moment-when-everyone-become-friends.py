from typing import List

class Solution:
    def getSuperParent(self, child, Parent):
        if child == Parent[child]:
            return child
        Parent[child] = self.getSuperParent(Parent[child], Parent)
        return Parent[child]
    
    def union(self, a, b, Parent, Rank):
        aParent = self.getSuperParent(a, Parent)
        bParent = self.getSuperParent(b, Parent)
        
        if aParent != bParent:
            if Rank[aParent] < Rank[bParent]:
                Parent[aParent] = bParent
                Rank[bParent] += Rank[aParent]
            else:
                Parent[bParent] = aParent
                Rank[aParent] += Rank[bParent]
            return True  # Successful union
        return False  # No union performed

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()  # Sort the logs by timestamp
        Parent = [i for i in range(n)]  # Parent array
        Rank = [1] * n  # Rank or size array
        
        components = n  # Initially, there are n components
        
        for time, a, b in logs:
            if self.union(a, b, Parent, Rank):
                components -= 1  # Decrement the count of components only if a union was performed
            
            if components == 1:
                return time
        
        return -1
