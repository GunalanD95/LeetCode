class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        stack = []
        
        res   = [0] * n
        prev_start_time = 0
        
        for log in logs:
            func_id , action , time = log.split(':')
            
            func_id = int(func_id)
            time    = int(time)
            
            if action == 'start':
                if stack:
                    res[stack[-1]] += time - prev_start_time
                stack.append(func_id)
                prev_start_time = time
            else:
                res[stack.pop()] += time - prev_start_time + 1
                prev_start_time = time + 1
                
        return res