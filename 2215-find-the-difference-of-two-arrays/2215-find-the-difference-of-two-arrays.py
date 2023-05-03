class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Map = Counter(nums1)
        nums2Map = Counter(nums2)
        a = [i for i in nums1Map if i not in nums2Map]
        b = [i for i in nums2Map if i not in nums1Map]
        return [a,b]
        