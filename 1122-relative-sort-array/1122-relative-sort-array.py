class Solution:
    def relativeSortArray(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        indxMap = Counter(A)
        OrdDict = defaultdict(int)

        for idx in range(len(B)):
            num = B[idx]
            if num in indxMap:
                OrdDict[num] = (idx,0)
        for num in A:
            if num in OrdDict:
                indx , val = OrdDict[num]
                OrdDict[num] = (indx,val+1)
            else:
                idx += 1
                OrdDict[num] = (idx,1)
            
        res = []  
        for num in OrdDict:
            key = num
            _ , count = OrdDict[num]
            if count == 0:
                res.append(key)
            else:
                while count != 0:
                    res.append(key)
                    count -= 1
                
                
        return res