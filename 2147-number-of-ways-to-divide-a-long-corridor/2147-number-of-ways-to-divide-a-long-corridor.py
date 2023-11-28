class Solution:
    def numberOfWays(self, corridor: str) -> int:
        op = 1 
        curr = 0
        plants = 0
        cnts  = Counter(corridor)
        if cnts['S']&1  == 1 or cnts['S'] < 2  : return 0
        
        for ch in corridor :
            if ch == 'S' :
                curr += 1
            elif curr == 2 :
                plants += 1
            if curr == 3 :
                if plants > 0 :
                    op *= (plants + 1)  
                curr = 1
                plants  = 0
        return op % (10**9 + 7)