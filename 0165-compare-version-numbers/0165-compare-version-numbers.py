class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        N , M = len(v1) ,len(v2)
        if N < M:
            v1 = v1 + ['0'] * (M-N)
        elif M < N:
            v2 = v2 + ['0'] * (N-M)
        
        
        for rev1,rev2 in zip(v1,v2):
            rev1 = int(rev1)
            rev2 = int(rev2)
            
            if rev1 > rev2:
                return 1
            elif rev2 > rev1:
                return -1
        
        return 0