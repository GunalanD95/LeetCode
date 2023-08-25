class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        
        N , M = len(s1) , len(s2)

        dp = [[False]* (M+1) for _ in range(N+1)]
        dp[N][M] = True

        for indx1 in range(N,-1,-1):
            for indx2 in range(M,-1,-1):
                if indx1 < N and s1[indx1] == s3[indx1 + indx2]:
                    dp[indx1][indx2] |= dp[indx1 +1][indx2]
                if indx2 < M and s2[indx2] == s3[indx1 + indx2]:
                    dp[indx1][indx2] |= dp[indx1][indx2 +1]


        return dp[0][0]