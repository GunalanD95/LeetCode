class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A , B = a,b
        A = list(A)
        B = list(B)

        A = [int(i) for i in A]
        B = [int(j) for j in B]

        N = len(A)
        M = len(B)

        if N !=  M:
            if N > M:
                while M < N:
                    B.insert(0,0)
                    N = len(A)
                    M = len(B)
            else:
                while N < M:
                    A.insert(0,0)
                    N = len(A)
                    M = len(B)
        s = len(A) - 1
        res = list(range(N))
        car = 0
        while s >= 0:
            # use mod and div to get the carry and calculate the sum
            res[s] = (A[s] + B[s] + car) % 2
            car = (A[s] + B[s] + car) // 2

            s -=  1

        if car == 1:
            res.insert(0,1)

        return "".join(str(i) for i in res)
        