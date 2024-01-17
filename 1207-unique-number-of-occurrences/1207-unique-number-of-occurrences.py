from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countMap = Counter(arr)
        values   = sorted(countMap.values())
        for count in range(1,len(values)):
            if values[count] == values[count-1]:
                return False
        return True