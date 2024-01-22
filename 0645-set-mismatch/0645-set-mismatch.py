from collections import Counter , defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        hmap = {i:0 for i in range(1,N+1)}
        for num in nums:
            hmap[num] += 1
        ans = [None,None]
        for num in hmap:
            if hmap[num] == 0:
                ans[1] = num
            elif hmap[num] > 1:
                ans[0] = num
        return ans