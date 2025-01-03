class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        pf = [0] * N
        pf[0] = nums[0]
        for i in range(1,N):
            pf[i] = nums[i] + pf[i-1]   
        
        total = 0
        for i in range(N-1):
            left_sum = pf[i]
            right_sum = pf[N-1] - pf[i]
            if left_sum >= right_sum:
                total += 1

        return total