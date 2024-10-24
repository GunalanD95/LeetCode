from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        N =  len(digits)
        
        res = []
        
        hashmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        def generate_all_combinations(indx, path):
            if indx >= N:
                if path:
                    res.append("".join(path))
                return 
        
            
            cur_num = digits[indx]
            
            for child in hashmap[cur_num]:
                path.append(child)
                generate_all_combinations(indx+1, path)
                path.pop()
            
        generate_all_combinations(0,[])
        return res