class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        memo = {}

        @cache
        def find_total_ways(steps, position):
            if steps == 0:
                return 1 if position == 0 else 0

            ways = 0
            if position > 0:
                ways += find_total_ways(steps - 1, position - 1)
            ways += find_total_ways(steps - 1, position)
            if position < arrLen - 1:
                ways += find_total_ways(steps - 1, position + 1)

            return ways % mod

        return find_total_ways(steps, 0)