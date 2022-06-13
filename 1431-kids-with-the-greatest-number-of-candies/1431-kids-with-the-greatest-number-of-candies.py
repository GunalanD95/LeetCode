class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        N = len(candies)
        max_num = max(candies)
        for i in range(N):
            if candies[i] + extraCandies >= max_num:
                res.append(True)
            else:
                res.append(False)
        return res
         