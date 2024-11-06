import bisect
from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        N   = len(nums)
        sorted_list = SortedList()
        for i in range(N-1,-1,-1):
            num = nums[i]
            idx = sorted_list.bisect_left(num)
            sorted_list.add(num)
            res.append(idx)
        return res[::-1]