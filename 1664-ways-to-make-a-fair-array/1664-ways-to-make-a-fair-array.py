class Solution:
    def waysToMakeFair(self, A: List[int]) -> int:
        N = len(A)
        def EVPF(A):
            EVPF = [0] * N
            EVPF[0] = A[0]
            for i in range(1,len(EVPF)):
                if i %2 == 0:
                    EVPF[i] = EVPF[i-1] + A[i]
                else:
                    EVPF[i] = EVPF[i-1]
            return EVPF
            
        def ODPF(A):
            PF = [0] * N
            PF[0] = 0
            for i in range(1,len(PF)):
                if i %2 != 0:
                    PF[i] = PF[i-1] + A[i]
                else:
                    PF[i] = PF[i-1]
            return PF
        c = 0

        PFE = EVPF(A)
        PFO = ODPF(A)       

        TE = 0
        T0 = 0

        for i in range(0,len(A)):
            if i == 0:
                TE = 0 + (PFO[N-1] - PFO[i])
                T0 = PFO[i]  + (PFE[N-1] - PFE[i])
            else:
                TE = PFE[i-1] + (PFO[N-1] - PFO[i])
                T0 = PFO[i-1] + (PFE[N-1] - PFE[i])
            
            if TE == T0:
                c += 1
            
        return(c)
