from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_Map = Counter(tasks)
        count = 0
        for i in task_Map:
            cur_val = task_Map[i]
            if cur_val <= 3 and cur_val >= 2:
                count += 1
                task_Map[i] = 0
            elif cur_val > 3:
                while cur_val > 0:
                    if cur_val % 3 >= 0:
                        cur_val -= 3
                    elif cur_val % 2 >= 0:
                        cur_val -= 2
                    else:
                        return -1
                    
                    count += 1
            else:
                return -1
                
        return count 