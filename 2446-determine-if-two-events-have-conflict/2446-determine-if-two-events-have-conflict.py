import datetime 

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        # We know that the events take place on the same day 
        # so we will find how many minutes have passed since the beginning of the day
        
        start_event1 = 60 * int(event1[0][0:2]) + int(event1[0][3:])
        finish_event1 =  60 * int(event1[1][0:2]) + int(event1[1][3:])
        
        start_event2 = 60 * int(event2[0][0:2]) + int(event2[0][3:])
        finish_event2 =  60 * int(event2[1][0:2]) + int(event2[1][3:])
        
        # since we don't know which event started first, let's check two cases
        
        if start_event1 <= start_event2 <= finish_event1 or start_event2 <= start_event1 <= finish_event2:
            return True
        else:
            return False
            