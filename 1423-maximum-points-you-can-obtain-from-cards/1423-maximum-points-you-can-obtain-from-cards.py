class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        
        if N == k:
            return sum(cardPoints)
        
        cur_sum = 0
        # taking first k elements
        for i in range(k):
            cur_sum += cardPoints[i]
            
        max_score = cur_sum
        # take from back and start removing from back
        k_idx = k-1
        l_idx = N-1 # taking from back
        for idx in range(N):
            cur_sum -= cardPoints[k_idx]
            cur_sum += cardPoints[l_idx]
            max_score = max(max_score,cur_sum)
                        
            k_idx -= 1
            if k_idx < 0:
                break
            
            l_idx -= 1
        return max_score