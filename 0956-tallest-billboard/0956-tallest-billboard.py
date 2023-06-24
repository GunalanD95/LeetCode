class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        dp = {0:0}  # imagine key is the difference of the heights between the 2 steels: the value is the shorter height of the steel
        for rod in rods:
            for diff, height in tuple(dp.items()):
                dp[diff+rod] = max(dp.get(diff+rod,0), height) 
                dp[abs(diff-rod)] = max(dp.get(abs(diff-rod),0), height+min(diff,rod))
        return dp[0]