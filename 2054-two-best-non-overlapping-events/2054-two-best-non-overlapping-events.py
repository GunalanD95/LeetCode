class Solution:
    # def binary_search()
    
    
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N =  len(events)
        events.sort() 
        end_times = [event[0] for event in events]
        
        suffix_max = [0] * N
        suffix_max[N-1] = events[N-1][2] 
        for i in range(N-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], events[i][2])
        
        
        
        max_res = 0
        for start, end, value in events:
            idx = bisect.bisect_left(end_times, end+1)
            if idx <= N-1:
                max_val_from_idx = suffix_max[idx]
                cur_sum = value + max_val_from_idx
                max_res = max(max_res, cur_sum)
            else:
                max_res = max(max_res,value)
        return max_res