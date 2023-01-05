class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        N      = len(points)
        if N == 1:
            return 1

        points.sort(key= lambda x: x[1])

        end = points[0][1]
        count = 1

        for i in range(1,N):
            cur_start = points[i][0]
            cur_end   = points[i][1]
            if cur_start > end:
                count += 1
                end    = cur_end

        return count
