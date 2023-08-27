class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo, stone_set = {}, set(stones)

        def jump(i, k):
            if i not in stone_set or k == 0:
                return False
            
            if i == stones[-1]:
                return True
            
            if (i,k) in memo:
                return memo[i,k]
            
            memo[i,k] = jump(i+k, k) or jump(i+k-1, k-1) or jump(i+k+1, k+1)
            return memo[i,k]
        
        return jump(1,1)