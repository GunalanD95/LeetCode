class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_idx = 0
        for od_idx in range(len(nums)):
            cur_num = nums[od_idx]
            if not (cur_num & 1):
                nums[od_idx] = nums[even_idx]
                nums[even_idx] = cur_num
                even_idx += 1
        return nums