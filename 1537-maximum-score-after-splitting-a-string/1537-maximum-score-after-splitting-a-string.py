class Solution:
    def maxScore(self, s: str) -> int:
        N  = len(s)
        one_count = s.count('1')
        zero_count = 0

        max_score = 0
        for idx in range(N-1):
            if s[idx] == '0':
                zero_count += 1
            else:
                one_count -= 1
            max_score = max(max_score,one_count+zero_count)
        return max_score
            



