from collections import Counter , defaultdict

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        for n in Counter(nums).values():

            if n == 1: return -1

            else: ans+= n//3 + (n%3 != 0)

        return ans   