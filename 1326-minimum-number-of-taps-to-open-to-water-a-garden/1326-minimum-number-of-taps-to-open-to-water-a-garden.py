from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        
        for i in range(len(ranges)):
            if ranges[i] == 0:
                continue
            intervals.append((max(0, i - ranges[i]), min(n, i + ranges[i])))
        
        intervals.sort()
        
        min_taps = 0
        curr_end = 0
        max_reachable = 0
        i = 0
        
        while i < len(intervals) and intervals[i][0] <= curr_end:
            while i < len(intervals) and intervals[i][0] <= curr_end:
                max_reachable = max(max_reachable, intervals[i][1])
                i += 1
            curr_end = max_reachable
            min_taps += 1
            
            if curr_end >= n:
                return min_taps
        
        return -1
