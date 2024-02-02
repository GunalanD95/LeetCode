from collections import deque

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        q = deque(list(range(1,10)))
        while q:
            cur_num = q.popleft()
            if cur_num >= low and cur_num <= high:
                ans.append(cur_num)
                
            last_digit = cur_num % 10
            if last_digit < 9:
                new_num = (cur_num * 10) + last_digit + 1
                q.append(new_num)
        
        return ans