"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        intervals = [[it.start,it.end] for interval in schedule for it in interval]
        intervals.sort()
        print("intervals",intervals)
        
        res = []
        start , end = intervals[0][0] , intervals[0][1]
        
        for i  in range(1,len(intervals)):
            cur_start = intervals[i][0]
            
            if cur_start > end:
                res.append(Interval(end,cur_start))
            
            end =  max(end,intervals[i][1])
            
            
        return res