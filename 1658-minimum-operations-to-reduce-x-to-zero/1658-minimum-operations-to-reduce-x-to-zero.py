class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        target = sum(nums) - x
        
        start_indx = 0
        found = False
        
        cur_sum , max_len = 0 , 0
        
        for end_indx in range(N):
            cur_sum += nums[end_indx]
            
            while start_indx <= end_indx and cur_sum > target:
                cur_sum -= nums[start_indx]
                start_indx += 1
                
            if cur_sum == target:
                found   = True
                max_len = max(max_len,end_indx - start_indx + 1 )
                
        return N - max_len if found else -1
        
        