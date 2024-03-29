class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        N = len(nums) - 1
        
        k = k % len(nums)
        
        def rev(A,st,end):
            s = st
            e = end
            while s <= e:
                temp = A[s]
                A[s] = A[e]
                A[e] = temp
                s += 1
                e -= 1
            return A


        rev(nums,0,N)
        rev(nums,0,k-1)
        rev(nums,k,N)
        
        return nums