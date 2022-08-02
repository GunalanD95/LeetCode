# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.s = s
        self.e = e

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)
        intervals.sort(key=lambda x: x[0])
        
        ans  = []
        
        for i in range(N):
            # no overlap 
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
                
            # overlap so update the latest added value
            else:
                ans[-1][0] = min(intervals[i][0],ans[-1][0])
                ans[-1][1] = max(intervals[i][1],ans[-1][1])
                
        return ans


    
    
    
        