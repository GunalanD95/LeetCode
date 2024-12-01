class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if N < d:  # Not enough jobs for the days
            return -1

        # Cache for memoization
        cache = {}

        def schedule_jobs(indx, cuts):
            # Base cases
            if cuts > d:  # Too many days
                return float('inf')
            if indx >= N:  # If all jobs are scheduled
                return 0 if cuts == d else float('inf')

            # Check cache
            if (indx, cuts) in cache:
                return cache[(indx, cuts)]

            # Recursive case
            max_job = 0
            min_diff = float('inf')
            for i in range(indx, N):
                max_job = max(max_job, jobDifficulty[i])  # Maximum for this day
                # Recur for the next day
                rest = schedule_jobs(i + 1, cuts + 1)
                min_diff = min(min_diff, max_job + rest)

            # Cache and return the result
            cache[(indx, cuts)] = min_diff
            return min_diff

        # Start recursion from index 0 with 0 cuts (days used)
        result = schedule_jobs(0, 0)
        return -1 if result == float('inf') else result
