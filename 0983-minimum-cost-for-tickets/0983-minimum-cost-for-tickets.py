class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = float('inf')

            for d,c in zip([1,7,30],costs):
                j = i

                # skip days , move pointer to next day
                while j < len(days) and days[j] < days[i] + d:
                    j += 1

                print(i,j)
                cache[i] = min(cache[i] , c + dfs(j))

            return cache[i]

        return dfs(0)