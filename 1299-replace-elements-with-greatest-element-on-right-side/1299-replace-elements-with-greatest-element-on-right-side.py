class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        
        max_val = arr[-1]
        arr[-1] = -1
        
        for i in range(N-2,-1,-1):
            cur_val = arr[i]
            arr[i]  = max_val
            max_val = max(max_val,cur_val)
            
        return arr
        