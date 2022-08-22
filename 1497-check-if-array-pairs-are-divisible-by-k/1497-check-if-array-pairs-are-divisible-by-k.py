class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        N = len(arr)
        
        check = N // 2
        

        remap = [0] * (k)
        for i in range(len(arr)):
            rem = arr[i] % k
            remap[rem] += 1
                
        if remap[0] & 1: return False
        
        pairs = 0
        
        i , j = 1 , k -1
        while i < j:
            if remap[i] != remap[j]:
                return False
            
            pairs += remap[i] 
            i += 1
            j -= 1
            
            
        if pairs > 0 and i==j:
            pairs += remap[i] // 2
        
        pairs += remap[0]//2
        
        print("ans",pairs,"check",check)
        if pairs == check:
            return True
        return False
        
        
        
        '''
        
        [5,3,10,1,-7,0,33,-1,10,8,-3,0,-10,47,-9,-6,38,8,5,38,-4,4,-5,-8,-4,0,-8,5,7,3,-3,0,6,8,47,39,35,39,4,9]
43
        '''