class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        N = len(nums)
        
        stack = []
        vstack = []
        
        for i in range(N):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)
                vstack.append(nums[i])
                
        ans = 0
        for i in range(N-1,-1,-1):
            while stack and nums[i] < nums[stack[-1]]:
                ans = max(ans, i - stack[-1] + 1)
                stack.pop()
                
        print("stack->",stack)
        print("vstack->",vstack)
        
                
        return ans
        