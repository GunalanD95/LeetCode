class Solution:
    def canChange(self, start: str, target: str) -> bool:
        N , M = len(start) , len(target)
        start_t    = [(i,c) for i,c in enumerate(start) if c in "LR"]
        target_t   = [(i,c) for i,c in enumerate(target) if c in "LR"]
        
        if len(start_t) != len(target_t):
            return False
        
        
        
        for (start_pos,s_char),(target_pos,t_char) in zip(start_t,target_t):
            if s_char != t_char:
                return False
            
            if s_char == 'L' and start_pos < target_pos:
                return False
            
            if s_char == 'R' and start_pos > target_pos:
                return False
            
        return True
        