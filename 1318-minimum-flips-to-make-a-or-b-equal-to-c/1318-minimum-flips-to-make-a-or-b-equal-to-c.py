class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        total_count = 0

        for i in range(32):
            mask  = 1 << i
            a_val = 1 if mask & a else 0
            b_val = 1 if mask & b else 0
            c_val = 1 if mask & c else 0

            if c_val == 0:
                if b_val == 1 and a_val == 1:
                    total_count += 2
                elif b_val == 1 or a_val == 1:
                    total_count += 1
            elif c_val == 1 and b_val == 0 and a_val == 0:
                total_count += 1


        return total_count