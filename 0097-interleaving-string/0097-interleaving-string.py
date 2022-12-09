class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        N , M = len(s1) , len(s2)
        @lru_cache(None)
        def recurBro(indx1 , indx2):
            if indx1 == N and indx2 == M:
                return True
            ans = False
            if indx1 < N and s1[indx1] == s3[indx1 + indx2]:
                ans |= recurBro(indx1 +1 , indx2 )
            if indx2 < M and s2[indx2] == s3[indx1 + indx2]:
                ans |= recurBro(indx1 , indx2 +1)
            return ans
        return recurBro(0,0)