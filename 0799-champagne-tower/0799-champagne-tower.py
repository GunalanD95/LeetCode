class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * 101 for _ in range(101)]  # Using a 2D array for dynamic programming
        dp[0][0] = poured
        
        for row in range(query_row + 1):
            for col in range(row + 1):
                if dp[row][col] >= 1:
                    excess = dp[row][col] - 1
                    dp[row][col] = 1
                    dp[row + 1][col] += excess / 2
                    dp[row + 1][col + 1] += excess / 2
        
        return dp[query_row][query_glass]