class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 
        ans = []
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            target = -(nums[i]) 
            while j < k:
                cur_sum =  nums[j] + nums[k]
                if cur_sum == target:
                    triplet = [-target,nums[j],nums[k]]
                    ans.append([-target,nums[j],nums[k]])
                    
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                        
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    j = j + 1
                    k = k - 1                    
                if cur_sum < target:
                    j = j + 1
                elif cur_sum > target:
                    k = k - 1
        return ans