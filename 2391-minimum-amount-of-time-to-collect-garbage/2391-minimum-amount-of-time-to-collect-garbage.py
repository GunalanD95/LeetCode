from collections import defaultdict

class Solution:
    def garbageCollection(self, garbage, travel):
        freq = defaultdict(int)

        for currGarbage in garbage:
            for char in currGarbage:
                freq[char] += 1

        ans = freq.get('M', 0) + freq.get('P', 0) + freq.get('G', 0)
        j = 0

        for currGarbage in garbage:
            for char in currGarbage:
                freq[char] -= 1

            if freq.get('M', 0) > 0:
                ans += travel[j]
            if freq.get('P', 0) > 0:
                ans += travel[j]
            if freq.get('G', 0) > 0:
                ans += travel[j]
            
            j += 1

        return ans