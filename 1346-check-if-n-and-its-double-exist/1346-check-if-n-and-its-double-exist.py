class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mapper = defaultdict(int)
        
        for num in arr:
            if num*2 in mapper or num/2 in mapper:
                return True
            mapper[num] += 1
            
        return False