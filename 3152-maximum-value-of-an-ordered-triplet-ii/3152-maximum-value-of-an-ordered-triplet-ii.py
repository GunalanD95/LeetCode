class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        max_vals  = []
        min_vals  = []

        max_val = nums[0]
        for num in nums:
            max_val = max(max_val,num)
            max_vals.append(max_val)

        max_right = [0] * N
        max_right[N-1] = nums[N-1]
        for k in range(N-2, -1, -1):
            max_right[k] = max(max_right[k+1], nums[k])

        max_val =0
        for j in range(1,N-1):
            if max_vals[j-1] > nums[j] and max_right[j+1] > 0:
                max_val = max(max_val,(max_vals[j-1]-nums[j]) * max_right[j+1])
        return max_val