class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)
        
        skill.sort()
        
        prev_sum = None
        cur_sum  = 0
        low = 0 
        high = N-1
        tot_prod = 0
        while low < high:
            cur_sum = skill[low] + skill[high]
            tot_prod += (skill[low] *  skill[high])
            if prev_sum and cur_sum != prev_sum:
                return -1
            prev_sum = cur_sum 
            low  += 1
            high -= 1
        
        
        
        return tot_prod