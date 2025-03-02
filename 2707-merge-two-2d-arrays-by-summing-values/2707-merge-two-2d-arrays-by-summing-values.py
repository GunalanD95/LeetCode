from collections import defaultdict
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hmap = defaultdict(int)
        for key,val in nums1+nums2:
            if key in hmap:
                hmap[key] += val
            else:
                hmap[key] = val
        ans = [[key,val] for key,val in hmap.items()]
        ans.sort()
        return ans
            
            