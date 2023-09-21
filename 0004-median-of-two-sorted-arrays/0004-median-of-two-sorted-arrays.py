class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        N = len(nums1)
        M = len(nums2)
        
        length = N + M
        check = ((N+M)//2) + 1
        
        bool = False
        
        if length & 1:
            ans = 0
            
        else:
            ans1 = 0
            ans = 0
            bool = True
        
        i , j = 0 , 0
        
        counter = 0
        val = 0
        while i <= N - 1 and j <= M - 1:
            
            if nums1[i] < nums2[j]:
                val = nums1[i]
                i += 1
            else:
                val = nums2[j]
                j += 1
                
            counter += 1
            if bool and counter == check - 1:
                ans1 = val
                
            if counter == check:
                ans = val
                
                if not bool:
                    return ans
                else:
                    return (ans+ans1)/2
                
                
                
        while i <= N-1:
            val = nums1[i]
            counter += 1
            i += 1
            if bool and counter == check - 1:
                ans1 = val
            if counter == check:
                ans = val
                
                if not bool:
                    return ans
                else:
                    return (ans+ans1)/2

        while j <= M-1:
            val = nums2[j]
            counter += 1
            j += 1
            if bool and counter == check - 1:
                ans1 = val
            if counter == check:
                ans = val
                
                if not bool:
                    return ans
                else:
                    return (ans+ans1)/2