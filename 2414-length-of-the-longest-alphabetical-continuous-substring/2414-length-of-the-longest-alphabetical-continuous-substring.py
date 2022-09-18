class Solution:
    def longestContinuousSubstring(self, s: str) -> int:

        max_len = 0
        cur_len = 0

        prev = ord(s[0])
        
        for i in range(1,len(s)):
            check = ord(s[i])
            
            if (prev + 1) == (check):
                cur_len += 1
                max_len = max(cur_len,max_len)

            else:
                cur_len = 0

            prev = check

        return max_len + 1          