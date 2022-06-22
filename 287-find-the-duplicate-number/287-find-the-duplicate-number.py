class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0
        for i in nums:
            if i == prev:
                return i
            prev = i
