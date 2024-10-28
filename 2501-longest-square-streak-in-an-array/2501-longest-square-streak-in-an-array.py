from collections import defaultdict

class Solution:
    
    
    
    def longestSquareStreak(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        
        
        # TLE
#         nums.sort()
#         n = len(nums)
#         dp = [1] * n
        
#         for i in range(1,n):
#             for j in range(i):
#                 if nums[i]  ==  nums[j] * nums[j]:
#                     dp[i] = max(dp[i],dp[j]+1)
                
#         ans = max(dp) 
#         return ans if ans > 1 else -1
    
    
    
        nums.sort()
        cache = defaultdict(int)
        nums_set = set(nums)
        max_len  = 1
        for num in nums:
            if num*num in cache:
                cur_len = cache[num] + cache[num*num]
                max_len = max(cur_len,max_len)
            else:
                count = 1
                while num * num in nums_set:
                    count += 1
                    num = num**2
                cache[num] = count
                max_len = max(cache[num],max_len)
                
        if max_len == 1:
            return -1
        return max_len
        