class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_max = (1 << 31) - 1
        int_min = -(1<< 31)
        
        dd = dividend
        dv = divisor

        sign = 0
        if dd < 0 or dv < 0:
            sign = -1
        if dd < 0 and dv < 0:
            sign = 1


        dd = abs(dd)
        dv = abs(dv)

        tot = 0
        q = 0
        for i in range(31,-1,-1):
            if (tot + (dv << i) <= dd):
                tot += dv << i
                q = q  | (1 << i)


        if sign < 0: return -q
        
        if q >= int_max or  q <= int_min: 
            return int_max
        else:
            return q
