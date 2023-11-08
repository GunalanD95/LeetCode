class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        xdiff , ydiff = abs(sx - fx) , abs(sy - fy)
        
        if xdiff == 0 and ydiff == 0 and t == 1:
            return False
        
        return (min(xdiff,ydiff) + abs(xdiff - ydiff) ) <= t