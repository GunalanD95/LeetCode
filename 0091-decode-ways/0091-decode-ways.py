from functools  import lru_cache
class Solution:
    def numDecodings(self, string: str) -> int:
        n = len(string)
        dp = [0] * (n+1)
        dp[n] = 1

        for indx in range(n-1,-1,-1):
            string_val = string[indx]

            if string_val != '0':
                dp[indx] += dp[indx+1]

            if indx + 1 < n and (string[indx] == '1' or string[indx] == '2' and string[indx + 1] <= '6'):
                dp[indx] += dp[indx+2]

        return dp[0]
        