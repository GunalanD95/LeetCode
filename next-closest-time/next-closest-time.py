from datetime import datetime

class Solution:
    def validate_time(self,time_str):
        pattern = re.compile(r'^([01]\d|2[0-3]):([0-5]\d)$')
        if pattern.match(time_str):
            return True
        else:
            return False
        

    def compare_times(self,time_str1, time_str2):
        time1 = datetime.strptime(time_str1, "%H:%M")
        time2 = datetime.strptime(time_str2, "%H:%M")
        if time1 > time2:
            return True
        return False
    
        
    def nextClosestTime(self, time: str) -> str:
        N      = len(time)
        digits = set()
        
        
        closet_time = time
        closed_diff = None
        
        next_day_time = time
        next_day_diff = None
        
        # get all the digits
        for num in time:
            if num.isalnum():
                digits.add(num)
        
        
        def check_all(indx,cur_time):
            nonlocal closed_diff , closet_time , next_day_diff , next_day_time
            if indx >= N:
                test_time = "".join(cur_time)
                if self.validate_time(test_time):
                    time1 = datetime.strptime(test_time, "%H:%M")
                    time2 = datetime.strptime(time, "%H:%M")
                    difference = time1 - time2
                    if self.compare_times(test_time,time):
                        if not closed_diff or difference < closed_diff:
                            closet_time = test_time
                            closed_diff = difference
                    else:
                        if test_time != time:
                            if not next_day_diff or difference < next_day_diff:
                                next_day_time = test_time
                                next_day_diff = difference                            

                return 
            
            if cur_time[indx] == ':':
                check_all(indx+1,cur_time)
            
            for i in range(indx,N):
                # for each position we have digits options so we can put them
                for digit in digits:
                    temp = cur_time[indx]
                    cur_time[indx] = digit
                    check_all(indx+1,cur_time)
                    cur_time[indx] = temp
                    
                    
        cur_time = list(time)
        # cur_day
        check_all(0,cur_time)
        if closet_time == time:
            return next_day_time
        
        return closet_time
            
            
            