from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)

        @lru_cache(None)
        def find_min_cost(indx):
            # Base case: If all days are covered, cost is 0
            if indx >= N:
                return 0
            
            # Start a new pass from the current travel day
            one_day_pass = find_min_cost(indx + 1) + costs[0]
            
            # 7-day pass: Find the next day not covered by the pass
            i = indx
            while i < N and days[i] < days[indx] + 7:
                i += 1
            seven_day_pass = find_min_cost(i) + costs[1]
            
            # 30-day pass: Find the next day not covered by the pass
            i = indx
            while i < N and days[i] < days[indx] + 30:
                i += 1
            thirty_day_pass = find_min_cost(i) + costs[2]
            
            # Return the minimum cost among the three options
            return min(one_day_pass, seven_day_pass, thirty_day_pass)
        
        # Start from the first travel day
        return find_min_cost(0)
