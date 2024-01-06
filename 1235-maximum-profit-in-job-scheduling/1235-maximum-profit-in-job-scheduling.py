class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit)))
        N = len(jobs)

        # Memoization to store already calculated results
        memo = {}

        def Solvethis(index):
            nonlocal memo

            if index in memo:
                return memo[index]

            if index >= N:
                return 0

            # don't take current job
            dont_take = Solvethis(index + 1)

            st, end, p = jobs[index]

            # find the next job that starts after the current job ends
            next_index = bisect_left(jobs, (end,))

            # take current job
            take_it = p + Solvethis(next_index)

            # update max_profit
            max_profit = max(dont_take, take_it)

            memo[index] = max_profit
            return max_profit

        return Solvethis(0)
