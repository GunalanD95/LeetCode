class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = int(1e9 + 7)
        
        @cache
        def dfs(index):
            if index >= len(s):
                return 1
            
            count = 0
            limit = min(index+10, len(s)) + 1
            for right in range(index+1, limit):
                sub = s[index:right]
                
                if sub.startswith("0") or int(sub) > k:
                    continue
                
                count += dfs(right)
                count %= MOD
            
            return count
        
        return dfs(0)