class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        A = nums
        N = len(A)
        if N == 1:
            return [A[0]]
        N3 = len(A) // 3
        me1 = A[0]
        me2 = A[1]
        c1 = 0
        c2 = 0
        for i in A:
            if i == me1:
                c1 += 1
            elif i == me2:
                c2 += 1
            else:
                if c1 == 0:
                    me1 = i
                    c1 = 1
                elif c2 == 0:
                    me2 = i
                    c2 = 1
                else:
                    c1 -= 1
                    c2 -= 1
        fe1 = 0
        fe2 = 0
        for j in A:
            if j == me1:
                fe1 += 1
            if j == me2:
                fe2 += 1
        res = []
        if me1 == me2:
            return [me1]
        else:
            if fe1 > N3:
                res.append(me1)
            if fe2 > N3:
                res.append(me2)
        return(res)