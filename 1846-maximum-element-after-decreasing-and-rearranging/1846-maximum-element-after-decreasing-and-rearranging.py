class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N = len(arr)
        
        if N == 1:
            return 1
        
        arr.sort()
        
        # first number is always 1
        max_val   = float('-inf')
        prev_val  = 1
        for idx in range(1,len(arr)):
            cur_val  = arr[idx]
            cur_diff = abs(prev_val - cur_val)
            
            if cur_diff > 1:
                if prev_val > cur_val:
                    cur_val = prev_val
                else:
                    cur_val = prev_val + 1

            prev_val = cur_val
            max_val  = max(max_val,cur_val)
            
        return max_val