class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N    = len(nums)

        pf   = [0] * (N)
        pf[0] = nums[0]
        for i in range(1,N):
            pf[i] = pf[i-1] + nums[i]

        sf    = [0] * (N)
        sf[-1] = nums[-1]
        for i in range(N-2,-1,-1):
            sf[i] = sf[i+1] + nums[i]

        ans = 0
        min_diff = float('inf')

        for i in range(N):
            val1_len = i + 1
            val2_len = N - i - 1
            val1_diff , val2_diff = 0 ,0

            if i+1  < N:
                val1_sum = pf[i]
                val2_sum = sf[i+1]

                val1_diff = val1_sum // val1_len
                val2_diff = val2_sum // val2_len
                
            else:
                val1_sum = pf[i]
                val2_sum = 0

                val1_diff = val1_sum // val1_len
                val2_diff = 0

            value = abs(val1_diff - val2_diff) 

            if value < min_diff:
                ans = i
                min_diff = value


        return ans 