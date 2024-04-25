class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        dp = [1] * N
        preMax = [0] * 26
        
        # first index in substring will always have a max len of 1 ( since its starting point)
        preMax[ord(s[0]) - ord('a')] = 1
        
        for i in range(1,N):
            cur_idx = ord(s[i]) - ord('a')
            for prev_idx in range(26):
                if abs(cur_idx - prev_idx) <= k:
                    dp[i] = max(dp[i] , 1 + preMax[prev_idx] )
                
            preMax[cur_idx] = max(preMax[cur_idx],dp[i])
            
        return max(dp)