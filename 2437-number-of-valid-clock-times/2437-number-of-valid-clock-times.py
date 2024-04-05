class Solution:
    def countTime(self, time: str) -> int:
        total_valid_time = 0
        
        def validate_time(time_str):
            try:
                hours, minutes = map(int, time_str.split(':'))
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    return True
                else:
                    return False
            except ValueError:
                return False        
        
        @cache
        def find_valid_clock_times(indx,cur_time):
            nonlocal total_valid_time
            if indx >= 5:
                if validate_time(cur_time):
                    total_valid_time += 1
                return 
                
            cur_pos_val = time[indx]
            if cur_pos_val == '?':
                for value in range(10):
                    find_valid_clock_times(indx+1,cur_time + str(value))
            else:
                # if its '?' then we might be try all possible valid answers
                find_valid_clock_times(indx+1,cur_time+ cur_pos_val)

                    
        find_valid_clock_times(0,'')
        return total_valid_time