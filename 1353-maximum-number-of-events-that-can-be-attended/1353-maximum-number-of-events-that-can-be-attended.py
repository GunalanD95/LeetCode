import heapq as hq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        
        total_days = max(event[1] for event in events)
        
        min_heap   = []
        
        day , ans , event_id = 0 , 0 , 0
        
        while day <= total_days:
            # if no events are available to attend today, let time flies to the next available event.
            if event_id < len(events) and not min_heap:
                day = events[event_id][0]
                
                
            # all events starting from today are newly avaiable . add them to the heap
            while event_id < len(events) and events[event_id][0] <= day:
                hq.heappush(min_heap,events[event_id][1])
                event_id += 1
                
            # if the event at heap top already ended, then discard it.
            
            while min_heap and min_heap[0] < day:
                hq.heappop(min_heap)
                
            # attend the event that will end the earliest
            if min_heap:
                hq.heappop(min_heap)
                ans += 1
                
            day += 1
            
            
        return ans 