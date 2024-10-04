from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)
        
        
        
        total_sum = sum(skill)
        
        target_sum  = total_sum // (len(skill)//2)
        
        skillMap = Counter(skill)
        
        print(target_sum)
        # if target_sum & 1: return -1
        
        
        total_prod = 0
        for num in skill:
            need_partner_skill = target_sum - num
            
            print(num,need_partner_skill)
            if need_partner_skill not in skillMap:
                return - 1
            
            
            skillMap[need_partner_skill] -= 1
            if skillMap[need_partner_skill] <= 0:
                del skillMap[need_partner_skill]
                
            
            total_prod += num * need_partner_skill
            

        return total_prod // 2