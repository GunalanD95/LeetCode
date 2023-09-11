class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        hmap = defaultdict(list)
        res  = []
        
        for idx,size in enumerate(groupSizes):
            if len(hmap[size]) < size:
                hmap[size].append(idx)
            else:
                res.append(hmap[size])
                hmap[size] = [idx]
        
        if hmap:
            for key in hmap:
                res.append(hmap[key])
        return res