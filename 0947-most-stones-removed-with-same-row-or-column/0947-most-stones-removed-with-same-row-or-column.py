class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graphX = defaultdict(list)
        graphY = defaultdict(list)
        
        for X,Y in stones:
            graphX[X].append(Y)
            graphY[Y].append(X)
            
        
        
        connectedComponent = 0
        visited = set()
        
        for x,y in stones:
            if (x,y) in visited:
                continue
            
            q = deque()
            q.append((x,y))
            
            while q:
                qx,qy = q.popleft()
                
                if (qx,qy) not in visited:
                    visited.add((qx,qy))
                    
                    for neiy in graphX[qx]:
                        q.append((qx,neiy))
                        
                    for neix in graphY[qy]:
                        q.append((neix,qy))
            
            
            connectedComponent += 1
        
        
        
        
        return len(stones) - connectedComponent

        