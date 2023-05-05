class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        hmap = defaultdict(int)
        N    = len(s)
        vowels = {'a','e','i','o','u'}
        
        
        max_val = 0
        q       = deque()
        for idx in range(k):
            if s[idx] in vowels:
                q.append(s[idx])
                
                
        res = len(q)
        left = 0
        for right in range(k,N):
            if q and q[0] == s[left]: 
                q.popleft()
                
            if s[right] in vowels:
                q.append(s[right])
            
            res = max(res,len(q))
            left += 1
            
        
        return res
        
        