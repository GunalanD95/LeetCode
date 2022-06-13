class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        N = len(nums)
        for i in range(N):
            for j in range(i+1,N):
                if nums[i] == nums[j]:
                    count += 1
        return count
        