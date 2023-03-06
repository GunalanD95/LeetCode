class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        N = arr[-1]
        
        if k > N:
            N = N + k
            
        ArrMap = Counter(arr)
        
        count = 0
        for i in range(1,N+1):
            if i not in ArrMap:
                count += 1     
                if count == k:
                    return i
        
        ans = 0
        for j in range(i+1,i+k+1):
            count += 1
            if count == k:
                return j
                
        