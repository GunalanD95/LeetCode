class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        idx = 1
        flag = False
        ans  = []
        while idx < N:
            num1,num2,num3 = nums[idx-1] ,nums[idx] ,nums[idx+1]
            
            if abs(num1-num2) > k or abs(num2-num3) > k or abs(num1-num3) > k:
                flag = True
                break
            
            
            ans.append([num1,num2,num3])
            
            idx += 3
        
        if flag: return []
        
        return ans