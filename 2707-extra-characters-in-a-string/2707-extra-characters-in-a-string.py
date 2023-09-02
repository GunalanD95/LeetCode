class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words=set(dictionary)
        n=len(s)
        @cache
        def solve(i):
            if i==len(s):
                return 0
            res=1+solve(i+1)
            for j in range(i,len(s)):
                if s[i:j+1] in words:
                    res=min(res,solve(j+1))
            return res
        return solve(0)