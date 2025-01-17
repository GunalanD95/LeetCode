class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        N = len(derived)
        # X ^ X =  0
        # X ^ 0 =  X
        # 0 ^ 1 = 1
        # A ^ B = C , B = A ^ C
        original = [None] * N
        original[0] = 0
        for i in range(1,N):
            original[i] = original[i-1] ^ derived[i-1]

        if original[N - 1] ^ original[0] == derived[-1]:
            return True

        original = [None] * N
        original[0] = 1
        for i in range(1,N):
            original[i] = original[i-1] ^ derived[i-1]

        if original[N - 1] ^ original[0] == derived[-1]:
            return True

        return False        

