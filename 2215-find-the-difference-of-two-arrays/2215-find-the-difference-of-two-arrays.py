class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_a = set(nums1)
        set_b = set(nums2)
        a = list(set_a.difference(set_b))
        b = list(set_b.difference(set_a))
        return [a,b]
        