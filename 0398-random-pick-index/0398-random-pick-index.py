from collections import defaultdict

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = defaultdict(list)
        for idx,num in enumerate(nums):
            self.nums[num].append(idx)
        print(self.nums)

    def pick(self, target: int) -> int:
        arr = self.nums[target]
        return random.choice(arr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)