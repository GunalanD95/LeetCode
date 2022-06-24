class Solution:
    def countBits(self, n: int) -> List[int]:
        def no_of_set_bits(n):
            cnt_1s = 0
            for i in range(32):
                mask = 1 << i
                if mask & n:
                    cnt_1s += 1
            return cnt_1s
        
        res = []
        for i in range(n+1):
            val = no_of_set_bits(i)
            res.append(val)
        return res