class Solution:
    def coloredCells(self, n: int) -> int:
        cur = 1
        for i in range(1,n):
            val = (4*i)
            cur += val
        return cur