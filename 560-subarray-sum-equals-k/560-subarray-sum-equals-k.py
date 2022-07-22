class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        N = len(nums)
        
        # BRUTEFORCE
#         count = 0
#         for i in range(N):
#             sum1 = 0
#             for j in range(i,N):
#                 sum1 += nums[j]
#                 if sum1 == k:
#                     count += 1
#         return count      

        hashmap = {}
        cur_sum = 0
        c = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum == k:
                c += 1

            if cur_sum - k in hashmap:
                c += hashmap[cur_sum - k]

            if cur_sum not in hashmap:
                hashmap[cur_sum] = 1
            else:
                hashmap[cur_sum] += 1
        return c
            
    
        
            
            
            
            
        
        