class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total_count = 0
        cur_count   = 0
        N = len(nums)
        for i in range(N):
            if nums[i] == 0:
                cur_count += 1
            else:
                cur_count = 0

            total_count += cur_count

        return(total_count)
        