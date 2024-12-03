class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_list = list(s)
        
        for idx in spaces:
            s_list[idx] = ' '+ s_list[idx]
            
        return ''.join(s_list)
        