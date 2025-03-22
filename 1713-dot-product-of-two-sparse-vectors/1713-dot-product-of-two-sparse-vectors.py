class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_map = {}
        for idx,num in enumerate(nums):
            if num > 0:
                self.index_map[idx] = num

    def dotProduct(self, vec: 'SparseVector') -> int:
        total_sum = 0
        map2 = vec.index_map
        for key,val in self.index_map.items():
            if key in map2:
                total_sum += (val * map2[key])
        return total_sum
        

