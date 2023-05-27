class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        
        @cache
        def letsgo(indx):
            if indx >= N:
                return 0
            
            max_diff = float('-inf')
            cur_diff = float('-inf')
            
            for i in range(1, min(4, N - indx + 1)):
                cur_score = sum(stoneValue[indx:indx+i])
                other_score = letsgo(indx + i)
                cur_diff = cur_score - other_score
                max_diff = max(max_diff, cur_diff)
                
            return max_diff
        
        diff = letsgo(0)
        
        if diff > 0:
            return 'Alice'
        elif diff < 0:
            return 'Bob'
        else:
            return 'Tie'
