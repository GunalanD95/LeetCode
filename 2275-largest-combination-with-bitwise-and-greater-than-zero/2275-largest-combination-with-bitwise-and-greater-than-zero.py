class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        N = len(candidates)
        
        max_len = 0
        
        for pos in range(32):
            mask = 1 << pos
            count = 0
            for num in candidates:
                if num & mask:
                    count += 1
                    
            max_len = max(max_len,count)
                
        return max_len
        