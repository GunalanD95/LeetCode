from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        left = 0
        count = 0
        max_val = max(nums)
        
        mapper = defaultdict(int)
        for right in range(N):
            if nums[right] == max_val:
                mapper[max_val] += 1
                
            while mapper[max_val] >= k:
                if nums[left] == max_val:
                    mapper[max_val] -= 1 
                count += N - right
                left  += 1                
                
        return count
