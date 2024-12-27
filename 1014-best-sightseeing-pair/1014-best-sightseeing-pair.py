import heapq as hq

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)        
        
        max_score = 0
        cur_max_so_far = values[0]
        values = values[1:]
        for idx,num in enumerate(values):
            idx += 1
            cur_val1 =  idx+num
            cur_val2 =  num-idx
            cur_score = cur_max_so_far + cur_val2
            cur_max_so_far = max(cur_max_so_far,cur_val1)
            max_score = max(max_score,cur_score)
        
        return max_score