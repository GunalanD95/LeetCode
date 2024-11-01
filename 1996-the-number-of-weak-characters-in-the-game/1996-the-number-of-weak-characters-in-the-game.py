class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1])) 
        
        max_defence = float('-inf')
        
        weaks = 0
        for _ , defence in properties:
            if defence < max_defence:
                weaks += 1
            else:
                max_defence = defence
        
        
        
        return weaks