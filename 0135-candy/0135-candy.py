class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        
        if N == 1: return 1

        candy = [1]* N
        st = N - 2

        while st >= 0:
            cur = ratings[st]
            if cur > ratings[st+1]:
                candy[st] = candy[st+1] + 1
            else:
                candy[st] = 1
            st -=1

        for i in range(1,N):
            if ratings[i] > ratings[i-1]:
                candy[i] = max(candy[i],candy[i-1] + 1)

        return sum(candy)