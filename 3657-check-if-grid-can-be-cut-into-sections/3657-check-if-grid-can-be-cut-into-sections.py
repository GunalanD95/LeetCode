from collections import defaultdict

class Solution:
    def count_non_intervals(self, intervals):
        count = 0
        prev = -1
        for start , end in intervals:
            if prev > start:
                pass
            else:
                count += 1
            prev = max(prev,end)
        return count


    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_map = []
        y_map = []


        for x1,y1,x2,y2 in rectangles:
            x_map.append([x1,x2])
            y_map.append([y1,y2])

        x_map.sort()
        y_map.sort()

        return True if max(
            self.count_non_intervals(x_map),
            self.count_non_intervals(y_map)
        ) >= 3 else False
        