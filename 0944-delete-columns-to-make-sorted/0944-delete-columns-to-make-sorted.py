class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N    = len(strs)
        K    = len(strs[0])


        colIndx = set()
        for j in range(K):
            pre = ord(strs[0][j])
            for i in range(1,N):
                cur = ord(strs[i][j])
                if cur < pre:
                    colIndx.add(j)
                pre = cur 
                
        return len(colIndx)        