class Solution:
    def maxScore(self, s: str) -> int:
        N  = len(s)
        pf = [0] * N
        sf = [0] * N
        pf[0] = 1 if s[0] == '0' else 0
        for i in range(1,N):
            if s[i] == '0':
                pf[i] = 1 + pf[i-1]
            else:
                pf[i] = pf[i-1]
        sf[0] = 0 if s[0] == '0' else 1
        for i in range(1,N):
            if s[i] == '1':
                sf[i] = 1 + sf[i-1]
            else:
                sf[i] = sf[i-1]
        max_score = 0
        for i in range(N-1):
            left_sum = pf[i]
            right_sum = sf[N-1] - sf[i]
            cur_score = left_sum + right_sum
            max_score = max(max_score,cur_score)
        return max_score


