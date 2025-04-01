class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)

        @lru_cache(None)
        def solve_this(indx):
            if indx >= N:
                return 0

            skip_indx = questions[indx][1]+1
            points    = questions[indx][0]

            take_it  =  points + solve_this(indx+skip_indx)
            dont_take = solve_this(indx+1)
            return max(take_it,dont_take)


        return solve_this(0)