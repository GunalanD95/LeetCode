class Solution:
    def minCut(self, s: str) -> int:
        string = list(s)
        N      = len(s)

        @lru_cache(None)
        def isPalindrome(l,r):
            if l >= r:
                return True
            if s[l] != s[r]:
                return False

            return isPalindrome(l+1,r-1)

        @lru_cache(None)
        def dp(indx):
            if indx == N:
                return 0 

            min_cuts = math.inf

            for j in range(indx,N):
                if isPalindrome(indx,j):
                    min_cuts = min(min_cuts , dp(j + 1) + 1)

            return min_cuts

        # print("dp",dp(0) -1)
        return dp(0) -1