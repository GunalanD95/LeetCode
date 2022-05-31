class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        A = nums
        N = len(A)
        def cPF(A):
            PF = list(range(0,N))
            PF[0] = A[0]
            for i in range(1,N):
                PF[i] = PF[i-1] + A[i]
            return PF

        PF = cPF(A)


        for i in range(0,N):

            LFS = 0 
            RFS = 0
            if i == 0:
                LFS = 0
                RFS = PF[N-1] - PF[i]
            else:
                LFS = PF[i-1]
                RFS = PF[N-1] - PF[i]

            if LFS == RFS:
                return i
        return -1