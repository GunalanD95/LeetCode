class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        N = len(satisfaction)
        satisfaction.sort(reverse=True) 
        pf = [0] * (N)
        pf[0] = satisfaction[0]
        for i in range(1,N):
            pf[i] = pf[i-1] + satisfaction[i]
        ans = 0
        cur_sum = 0
        for num in pf:
            cur_sum += num
            ans = max(ans,cur_sum)
        return ans 
        
        