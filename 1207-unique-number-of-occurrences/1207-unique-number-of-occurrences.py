class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        N = len(arr)
        
        
        res = dict()
        
        for i in range(len(arr)):
            if arr[i] not in res:
                res[arr[i]] = 1  
            else:
                res[arr[i]] += 1
            
        s = set()
        
        for k in res:
            if res[k] not in s:
                s.add(res[k])
            else:
                return False
            
        return True
        
        
        
        
        
        
        