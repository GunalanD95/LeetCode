class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)
        
        DP = [[-1] * (k+1) for _ in range(N+1)]
        
        
        def KnapSack(pile_indx: int,K : int) -> int:
            if pile_indx >= N or K == 0:
                return 0
            
            
            if DP[pile_indx][K] != -1:
                return DP[pile_indx][K] 
            
            
            #Dont_take
            dont_include = KnapSack(pile_indx+1,K)
            
            
            #Include
            include        = 0
            cur_piles_tkn  = 0
            
            for i in range(min(K,len(piles[pile_indx]))):
                cur_piles_tkn += piles[pile_indx][i]
                
                include        = max(include , 
                                 cur_piles_tkn + KnapSack(pile_indx+1 , K - i - 1))
                
            
            DP[pile_indx][K]   = max(include,dont_include)
            
            return DP[pile_indx][K] 
        
        return KnapSack(0,k)
        
        
            
        