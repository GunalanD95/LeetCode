class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = 0
        for i in range(m,len(nums1)):
            nums1[i] = nums2[count]
            count += 1
            
        for i in range(0,len(nums1)):
            for j in range(i+1,len(nums1)):
                if nums1[i] > nums1[j]:
                    temp = nums1[i]
                    nums1[i] = nums1[j]
                    nums1[j] = temp
        