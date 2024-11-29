class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        
        @cache
        def DP(indx):
            if indx >= N:
                return 0
            
            # Calculate the cost if we start at the current index
            take_step1 = cost[indx] + DP(indx + 1)
            take_step2 = cost[indx] + DP(indx + 2)
            
            # Return the minimum cost of either taking step 1 or step 2
            return min(take_step1, take_step2)
        
        # Start from the first step (index 0) and return the minimum cost
        return min(DP(0), DP(1))