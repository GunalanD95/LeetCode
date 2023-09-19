class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
#         seen = [0] * (len(nums))
#         for num in nums:
#             if seen[num]:
#                 return(num)
#             seen[num] = 1
            
# --------------------------------------------------------------------------------------------------------
#         hashmap = {}
#         for i in nums:
#             if i not in hashmap:
#                 hashmap[i] = 1
#             else:
#                 hashmap[i] += 1
                
                
#         for i in hashmap:
#             if hashmap[i] > 1:
#                 return i
# --------------------------------------------------------------------------------------------------------

        slow , fast  = 0 , 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
                
                
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
                
        return slow
