class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = int(1e9) + 7

        # Create a 3D array to store the number of paths for each position and remaining moves
        dp = [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        def friday(i, j, cur_moves):
            # Base case: if out of boundary, return 1
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            # Base case: if no more moves left, return 0
            if cur_moves == 0:
                return 0

            # Check if the result for this position and remaining moves is already calculated
            if dp[i][j][cur_moves] != -1:
                return dp[i][j][cur_moves]

            # Explore all possible moves and calculate the total paths
            total_paths = (friday(i + 1, j, cur_moves - 1) +
                           friday(i - 1, j, cur_moves - 1) +
                           friday(i, j + 1, cur_moves - 1) +
                           friday(i, j - 1, cur_moves - 1)) % MOD

            # Store the result in the dp array
            dp[i][j][cur_moves] = total_paths

            return total_paths


        # Start the recursive function
        result = friday(startRow, startColumn, maxMove)

        return result % MOD

