class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        MAX_NUM = num
        print("Nums",nums)
        N = len(nums)
        if N == 1:
            return num
        max_number_idx = N-1
        for idx in range(N-2,-1,-1):
            if nums[idx] > nums[max_number_idx]:
                max_number_idx = idx
            else:
                nums[idx] , nums[max_number_idx] = nums[max_number_idx] , nums[idx]
                print("nums",nums)
                CUR_NUM = "".join(nums)
                CUR_NUM = int(CUR_NUM)
                MAX_NUM = max(MAX_NUM,int(CUR_NUM))
                nums[max_number_idx] , nums[idx] = nums[idx] , nums[max_number_idx]
        return MAX_NUM