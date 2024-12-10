class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)
        
        substrings =  defaultdict(int)
        
        for i in range(N):
            for j in range(i + 1, N + 1):
                substrings[s[i:j]] += 1  
        
        max_length = 0
        for string in substrings:
            if substrings[string] >= 3 and len(set(string)) == 1:
                max_length = max(max_length,len(string))
        return -1 if max_length == 0 else max_length