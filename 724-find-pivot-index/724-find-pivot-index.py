class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        
        def cPF(A):
            N = len(A)
            PF = [0] * len(A)
            PF[0] = A[0]
            prev = A[0]
            for i in range(1,N):
                PF[i] = A[i] + prev
                prev = PF[i]
                
            return PF
        
        PF = cPF(nums)
        
        for i in range(N):
            if i == 0:
                leftsum = 0
                rightsum = PF[N-1] - PF[i]
            elif i == N:
                leftsum = PF[i-1]
                rightsum = 0
            else:
                leftsum = PF[i-1]
                rightsum = PF[N-1] - PF[i]
                
            if leftsum == rightsum:
                return i
            
        return -1