from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)
    
    def atMostK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        freq = defaultdict(int)
        left = 0
        
        for right in range(n):
            if freq[nums[right]] == 0:
                k -= 1
            freq[nums[right]] += 1
            
            while k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    k += 1
                left += 1
            
            count += right - left + 1
        
        return count
