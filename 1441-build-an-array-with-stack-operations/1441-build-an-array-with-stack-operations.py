class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res = []
        
        num     = 1
        pointer = 0
        while num <= n and pointer < len(target):
            
            if num == target[pointer]:
                res.append("Push")
                pointer += 1
            else:
                res.append("Push")
                res.append("Pop")
                
            num += 1
        
        return res
        