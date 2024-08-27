class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        N = len(s)
        hmap = dict()
        
        
        last_seen_indx = -1
        max_unq_len = 1
        
        for cur_indx in range(N):
            cur_char = s[cur_indx]
            if cur_char in hmap:
                last_seen_indx = max(last_seen_indx,hmap[cur_char])
            max_unq_len = max(max_unq_len,cur_indx - last_seen_indx)
            hmap[cur_char] = cur_indx
            
        return max_unq_len