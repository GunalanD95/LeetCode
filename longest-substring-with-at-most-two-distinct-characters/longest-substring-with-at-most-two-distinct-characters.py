from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        N = len(s)
        K = 2
        
        left = 0
        right = 0
        
        smap    = defaultdict(int)
        max_len = 0
        
        while right <  N:
            right_char = s[right]
            smap[right_char] += 1
            
            while len(smap) > K:
                smap[s[left]] -= 1
                if smap[s[left]] <= 0:
                    del smap[s[left]]
                left += 1
            
            
            cur_len = right - left + 1
            max_len = max(max_len,cur_len)
            
            right += 1
            
        return max_len