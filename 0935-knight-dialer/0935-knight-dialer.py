class Solution:
    def knightDialer(self, n: int) -> int:
        graph = collections.defaultdict(list)
        graph[0].extend([4, 6])
        graph[1].extend([6, 8])
        graph[2].extend([7, 9])
        graph[3].extend([4, 8])
        graph[4].extend([3, 9, 0])
        graph[5].extend([])
        graph[6].extend([0, 7, 1])
        graph[7].extend([2, 6])
        graph[8].extend([1, 3])
        graph[9].extend([4, 2])
        MOD = int(1e9 + 7)
        
        @cache
        def dfs(digit, need):
            if need == 0:
                return 1
            
            count = 0
            
            for nei in graph[digit]:
                count += dfs(nei, need - 1)
                count %= MOD
            
            return count
        
        return sum(dfs(digit, n-1) for digit in range(10)) % MOD