class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)
        
        # Step 1: Compute LCS using DP
        dp = [["" for _ in range(M + 1)] for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

        lcs = dp[N][M]  # Get the longest common subsequence

        # Step 2: Build SCS from str1, str2, and LCS
        i, j = 0, 0
        final = ""

        for c in lcs:
            while i < N and str1[i] != c:  # Add non-LCS chars from str1
                final += str1[i]
                i += 1
            while j < M and str2[j] != c:  # Add non-LCS chars from str2
                final += str2[j]
                j += 1
            final += c  # Add the LCS character
            i += 1
            j += 1

        # Add remaining characters
        final += str1[i:] + str2[j:]

        return final
