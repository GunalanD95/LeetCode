class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = int(1e9) + 7
        n = len(locations)
        
        # Initialize dp array
        dp = [[-1] * (fuel + 1) for _ in range(n)]
        
        def countRoutesDP(cur_city, cur_fuel):
            if cur_fuel < 0:
                return 0
            
            if dp[cur_city][cur_fuel] != -1:
                return dp[cur_city][cur_fuel]
            
            count = 0
            if cur_city == finish:
                count = 1
            
            for next_city in range(n):
                if next_city != cur_city:
                    fuel_needed = abs(locations[cur_city] - locations[next_city])
                    if cur_fuel >= fuel_needed:
                        count = (count + countRoutesDP(next_city, cur_fuel - fuel_needed)) % MOD
            
            dp[cur_city][cur_fuel] = count
            return count
        
        return countRoutesDP(start, fuel)
