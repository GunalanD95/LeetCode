class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N   = len(s)
        
        if N > 12: return []
        
        
        res = []
        string = ''
        
        def backtracking(indx,dots,ipaddress):
            if dots == 4 and indx >= N:
                res.append(ipaddress[:-1])
                return 
            
            if dots > 4:
                return 
            
            
            for j in range(indx,min(N,indx+3)):
                if int(s[indx:j+1]) <= 255 and (indx == j or s[indx] != '0'):
                    backtracking(j+1,dots+1,ipaddress + s[indx:j+1] + '.')

                
                
        backtracking(0,0,'')
        return res