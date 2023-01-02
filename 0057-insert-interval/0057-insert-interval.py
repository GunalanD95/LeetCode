class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)

        res = []

        # since the input is sorted 1 - we can test ending time is lesser than new interval
        i  = 0
        while i < N and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # now merge overlapping intervals
        while i < N and intervals[i][0] <= newInterval[1]:
            st = min(intervals[i][0],newInterval[0])
            ed = max(intervals[i][1],newInterval[1])
            newInterval = [st,ed]
            i += 1     

            
        
        res.append(newInterval)

        # push back rest
        while i < N:
            res.append(intervals[i])
            i += 1

        return res      