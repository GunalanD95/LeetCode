class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        m = len(pizza)
        n = len(pizza[0])

        # dp[k][r][c] represents the number of ways to cut the remaining pizza into k pieces
        # starting from row r and column c
        dp = [[[None] * n for _ in range(m)] for _ in range(k)]

        # preSum[r][c] is the total number of apples in pizza[r:][c:]
        preSum = [[0] * (n+1) for _ in range(m+1)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                preSum[r][c] = preSum[r+1][c] + preSum[r][c+1] - preSum[r+1][c+1] + (pizza[r][c] == 'A')

        # Start the recursive function dfs with initial parameters
        # m = number of rows, n = number of columns, k = number of pieces we need to cut the pizza into,
        # r = row index where we start cutting, c = column index where we start cutting
        return self.dfs(m, n, k-1, 0, 0, dp, preSum)

    # Recursive function to compute the number of ways to cut the remaining pizza into k pieces
    def dfs(self, m, n, k, r, c, dp, preSum):
        # If the remaining piece has no apple, then it is an invalid cut and we return 0
        if preSum[r][c] == 0:
            return 0
        # If we have found a valid way to cut the pizza into k pieces, then we return 1
        if k == 0:
            return 1
        # If the dp array already contains the number of ways to cut the remaining pizza into k pieces
        # starting from row r and column c, then we return the value from the dp array
        if dp[k][r][c] is not None:
            return dp[k][r][c]
        ans = 0
        # Cut the pizza horizontally at position nr if the upper piece contains at least one apple
        for nr in range(r+1, m):
            if preSum[r][c] - preSum[nr][c] > 0:
                ans = (ans + self.dfs(m, n, k-1, nr, c, dp, preSum)) % 1000000007
        # Cut the pizza vertically at position nc if the left piece contains at least one apple
        for nc in range(c+1, n):
            if preSum[r][c] - preSum[r][nc] > 0:
                ans = (ans + self.dfs(m, n, k-1, r, nc, dp, preSum)) % 1000000007
        # Memoize the result in the dp array and return the result
        dp[k][r][c] = ans
        return ans