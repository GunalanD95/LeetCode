class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N  = len(senate)
        
        q1 = deque()
        q2 = deque()
        
        for idx,char in enumerate(senate):
            if char == 'R':
                q1.append(idx)
            else:
                q2.append(idx)
                
        
        while q1 and q2:
            r = q1.popleft()
            d = q2.popleft()
            
            if r <= d:
                q1.append(r+N)
            else:
                q2.append(d+N)
                
        if len(q1) >= len(q2):
            return 'Radiant'
        return 'Dire'