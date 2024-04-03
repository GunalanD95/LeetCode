import heapq as hq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        available_rooms = [room for room in range(n)]
        used_rooms      = [] # (end_time ,room_number)
        count = [0] * n
        
        
        for start,end in meetings:
            
            # if there are used room and we are checking current start with latest end meeting
            while used_rooms and start >= used_rooms[0][0]:
                _ , room =  hq.heappop(used_rooms)
                # now this room is free lets push to available_rooms
                
                hq.heappush(available_rooms,room)
                
                
            # if rooms are free , then assign the current meetigs
            if available_rooms:
                room = hq.heappop(available_rooms)
                count[room] += 1
                hq.heappush(used_rooms,(end,room))
            else:
                # no room is free 
                end_time , room = hq.heappop(used_rooms)
                duration = end - start 
                hq.heappush(used_rooms,(end_time + duration ,room))
                count[room] += 1
                
                
                
                
                
        max_val = max(count)
        max_idx = count.index(max_val)
        print(count)
        return max_idx
        