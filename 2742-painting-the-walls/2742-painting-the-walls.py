class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n=len(cost)
        @cache
        def dp(idx,t):
            if idx==n: return 0 if t>=0 else sys.maxsize
            #this index painted by paid painter
            ans=cost[idx]+dp(idx+1,min(n+1,t+time[idx]))
            #free painter
            ans=min(ans,dp(idx+1,t-1))
            return ans
        return dp(0,0)