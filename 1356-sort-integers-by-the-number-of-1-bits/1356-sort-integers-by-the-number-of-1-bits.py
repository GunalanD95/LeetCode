from collections import defaultdict
class Solution:
    def countSetBits(self, num):
        return bin(num).count('1')
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        res    = []
        
        setMap = defaultdict(list)
        
        for num in arr:
            setMap[self.countSetBits(num)].append(num)
            
        for ls in sorted(setMap.keys()):
            setMap[ls].sort()
            res.extend(setMap[ls])
        return res