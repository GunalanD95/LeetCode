class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        N = len(nums)
        
        stack = []
        max_dis = 0
        
        
        for i in range(N):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
                
                
        for j in range(N-1,-1,-1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_dis = max(max_dis,j -i)
        
        return max_dis