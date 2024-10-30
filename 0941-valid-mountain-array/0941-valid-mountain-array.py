class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        
        if N <= 2: return False
        
        mid_indx = 0
        
        prev = arr[0]
        for i in range(1,N):
            if prev < arr[i]:
                prev = arr[i]
            else:
                mid_indx = i-1
                break
                
        if mid_indx == 0:
            return False
        print(arr[mid_indx],mid_indx)
        
        prev = arr[mid_indx]
        
        for i in range(mid_indx+1,N):
            cur = arr[i]
            if cur >= prev:
                print(cur,prev,"here")
                return False
            
            prev = cur
        
        
        
        
        return True