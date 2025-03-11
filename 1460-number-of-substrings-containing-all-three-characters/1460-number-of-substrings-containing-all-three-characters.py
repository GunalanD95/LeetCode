from collections import defaultdict , Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        counter = defaultdict(int)
        left  = 0
        right = 0
        total = 0
        while right < N:
            counter[s[right]] += 1

            while len(counter) == 3:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]] 
                total += N - right
                left  += 1  
            
            right += 1

        return total