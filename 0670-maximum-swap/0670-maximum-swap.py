class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        last_occurence = {int(num):idx for idx,num in enumerate(nums)}

        for idx in range(len(nums)):
            cur_num = int(nums[idx])
            for number in range(9,cur_num,-1):
                if number in last_occurence and last_occurence[number] > idx:
                    nums[idx],nums[last_occurence[number]] = nums[last_occurence[number]],nums[idx]
                    return int("".join(nums))

        
        return num