class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        return self.dfs(N, K, W, 0, {})
    
    def dfs(self, N, K, W, cur, memo):
        
        if cur == K-1:
            return min(N-K+1, W) / W
        if cur > N:
            return 0
        elif cur >= K:
            return 1.0
        
        if cur in memo:
            return memo[cur]
        
        prob = self.dfs(N, K, W, cur+1, memo) - (self.dfs(N, K, W, cur+1+W, memo) - self.dfs(N, K, W, cur+1, memo)) / W
        
        memo[cur] = prob
        
        return prob