class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N = len(s)

        ans = set()
        seen = set()
        def backtracking(indx, cur_string):
            if indx + 10 > N:
                return 

            if cur_string in seen:
                ans.add(cur_string)
            else:
                seen.add(cur_string)
            
            if indx+10 < N:
                backtracking(indx+1, cur_string[1:] + s[indx+10])

        backtracking(0, s[:10])

        return list(ans)
        