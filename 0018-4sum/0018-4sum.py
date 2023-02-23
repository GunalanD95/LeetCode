class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        if N < 4: 
            return []
        if N == 4:
            if sum(nums) == target: 
                return [nums] 
            else:
                return []    
        
        ans = []
        for i in range(N-3):
            numI = nums[i]
            
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            for j in range(i+1,N-2):
                numJ = nums[j]
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                
                to_find = target -(numI + numJ)
                
                low  = j + 1
                high = N - 1
                
                while low < high:
                    cur_sum = nums[low] + nums[high]
                    
                    if cur_sum == to_find:
                        print("ans",ans)
                        ans.append([numI,numJ,nums[low],nums[high]])

                        while low < high  and nums[low] == nums[low+1]:
                            low += 1

                        while low < high and nums[high] == nums[high-1]:
                            high -= 1

                        low += 1
                        high -= 1

                        
                    if cur_sum > to_find:
                        high -= 1
                    elif cur_sum < to_find:
                        low  += 1
                        
        return ans
                