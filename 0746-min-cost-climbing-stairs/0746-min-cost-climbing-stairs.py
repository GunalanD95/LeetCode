class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        
        @cache
        def DP(indx):
            if indx >= N:
                return 0
            
            step1 = cost[indx] + DP(indx + 1)
            step2 = cost[indx] + DP(indx + 2)
        
            return min(step1, step2)
        
        return min(DP(0), DP(1))