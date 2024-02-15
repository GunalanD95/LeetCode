class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        cur_sum   = nums[0]
        
        N = len(nums)
        
        total_len = 1
        last_added_value = [nums[0]]
        
        for idx in range(1,N):
            num = nums[idx]
            if num >= last_added_value[-1]:
                cur_sum += num
                total_len += 1
                last_added_value.append(num)
        while last_added_value and (cur_sum - last_added_value[-1]) <= last_added_value[-1]:
            cur_sum = cur_sum - last_added_value[-1]
            total_len -= 1
            last_added_value.pop()
        
        
        if total_len < 3:
            return -1
        
        return cur_sum