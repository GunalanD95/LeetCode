class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n, m = len(target), len(words[0])
        
        # Create position map - count of each char at each position
        pos_count = defaultdict(lambda: defaultdict(int))
        for word in words:
            for idx, char in enumerate(word):
                pos_count[idx][char] += 1
        
        @cache
        def dp(i, k):
            # Finished target string
            if i == n:
                return 1
            # No more positions left but target not finished
            if k == m:
                return 0
                
            # Don't use current position
            ways = dp(i, k + 1)
            
            # Use current position if target char exists
            cur_char = target[i]
            if pos_count[k][cur_char] > 0:
                ways += pos_count[k][cur_char] * dp(i + 1, k + 1)
                
            return ways % MOD
            
        return dp(0, 0)