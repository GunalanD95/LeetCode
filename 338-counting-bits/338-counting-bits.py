class Solution:
    def countBits(self, n: int) -> List[int]:
        check = [0]
        for i in range(1,n+1):
            val = i % 2
            check.append(check[i//2] + val)
        return check