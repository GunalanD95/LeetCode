class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        N = len(s)
        
        hmap = {}
        ans = 0
        
        start = -1
        
        for i in range(N):
            val = s[i]
            if val in hmap: 
                prev = hmap[val]
                start = max(prev,start)
            ans = max(ans, i- start)
            hmap[val] = i
            
            
        return ans
                