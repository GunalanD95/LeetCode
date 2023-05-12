class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        N = len(questions)
        
        memo = {}
        
        def PassMe(indx):
            if indx >=  N:
                return 0
            
            if indx in memo:
                return memo[indx]
            
            score  = questions[indx][0]
            nxtQ   = questions[indx][1]
            
            # dont_solve 
            ans1 = PassMe(indx+1)
            # solved_it 
            ans2 = score + PassMe(indx+1+nxtQ)
            
            memo[indx] = max(ans1, ans2)
            
            return memo[indx]
            
            
        return PassMe(0) 