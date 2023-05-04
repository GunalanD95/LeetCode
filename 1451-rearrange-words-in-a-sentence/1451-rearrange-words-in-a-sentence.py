class Solution:
    def arrangeWords(self, text: str) -> str:
        
        res  = text.lower().split(' ')
        res.sort(key = lambda x: len(x))
        res[0] = res[0].capitalize()
        string = ' '.join(res)
        return string 
        
        
        