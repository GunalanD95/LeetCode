class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        N = len(nums) - 1
        

        def Rev(A,st,end):
            s = st
            e = end

            while s <= e:
                temp = A[s]
                A[s] = A[e]
                A[e] = temp

                s += 1
                e -= 1
            return A

        Rev(nums,0,N)
        Rev(nums,0,k-1)
        Rev(nums,k,N)
        
        return nums