class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        N = len(nums)
        
        # BruteForce 
#         for i in range(N):
#             for j in range(i+1,N):
#                 if nums[i] == nums[j]:
#                     count += 1
#         return count
    
    
        # Optimized 
        
        hashmap = {}
        s = N - 1
        while s >= 0:
            if nums[s] not in hashmap:
                hashmap[nums[s]] = 1
            else:
                count += hashmap[nums[s]]
                hashmap[nums[s]] += 1
                
            s -= 1
        return count
                
            
        