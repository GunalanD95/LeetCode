class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        stack = []
        stack.append(N-1)

        ans   = [0] * N
        for i in range(N-2,-1,-1):
            cur_temp   =  temperatures[i]
            while stack and cur_temp >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = (stack[-1]) -i 
                
            stack.append(i)
            
        return ans 