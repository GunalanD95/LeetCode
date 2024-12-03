from collections import defaultdict

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # DP table: dp[indx][hoods][color]
        # Default to infinity for invalid states
        prev_dp = defaultdict(lambda: float('inf'))
        prev_dp[(0, 0)] = 0  # Start with 0 cost, 0 neighborhoods, and no color
        
        for i in range(m):
            curr_dp = defaultdict(lambda: float('inf'))
            
            for (hoods, pre_color), cur_cost in prev_dp.items():
                if houses[i] != 0:
                    # House is already painted
                    cur_color = houses[i]
                    if cur_color != pre_color:
                        curr_dp[(hoods + 1, cur_color)] = min(curr_dp[(hoods + 1, cur_color)], cur_cost)
                    else:
                        curr_dp[(hoods, cur_color)] = min(curr_dp[(hoods, cur_color)], cur_cost)
                else:
                    # House is not painted; try all colors
                    for color in range(1, n + 1):
                        if color != pre_color:
                            curr_dp[(hoods + 1, color)] = min(curr_dp[(hoods + 1, color)], cur_cost + cost[i][color - 1])
                        else:
                            curr_dp[(hoods, color)] = min(curr_dp[(hoods, color)], cur_cost + cost[i][color - 1])
            
            prev_dp = curr_dp  # Move to the next house
        
        # Find the minimum cost among valid states
        min_cost = float('inf')
        for (hoods, color), cost in prev_dp.items():
            if hoods == target:
                min_cost = min(min_cost, cost)
        
        return -1 if min_cost == float('inf') else min_cost
