class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans  = []
        
        for i in range(len(meetings)):
            # no overlap 
            if not ans or ans[-1][1] < meetings[i][0]:
                ans.append(meetings[i])
                
            # overlap so update the latest added value
            else:
                ans[-1][0] = min(meetings[i][0],ans[-1][0])
                ans[-1][1] = max(meetings[i][1],ans[-1][1])
        prev_start , prev_end = None , None
        for st,end in ans:
            days -= ( end - st  + 1)
            prev_start , prev_end = st , end
        return days