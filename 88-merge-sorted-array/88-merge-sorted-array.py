class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # insert index 
        k = m + n - 1

        # merge values 
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[k] = nums1[m-1]
                m -= 1
            else:
                nums1[k] = nums2[n-1]
                n -= 1
            k -= 1
            
        # inserting left over value from nums2 to num1 head
        while n > 0:
            nums1[k] = nums2[n-1]
            k -= 1
            n -= 1

                
                
        '''
        approach : https://www.youtube.com/watch?v=P1Ic85RarKY
        
        '''
                
        
        